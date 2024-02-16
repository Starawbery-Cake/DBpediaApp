import unicodedata
import PySimpleGUI as sg
import quereis
from quereis import do_inquiry
import reshapeResults
import myfunc
import manipulate_tree
import manipulate_graph
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal


def unique_value_generator(start_value=0):
    current_value = start_value
    while True:
        yield current_value
        current_value += 1


def main():
  ImgKey = "img"
  InduceSearchTextKey = "induce"
  SearchBoxKey = "search_word"
  DoSearchKey = "do_search"
  AbstTitleKey = "abst_title"
  AbstTextKey = "abst"
  ErrorTextKey = "error"
  ChoiceFromListKey = "choise_from_list"
  ListBoxTitle = "list_title"
  ListBoxKey = "listBox"

  search_mode:Literal["keyword", "ID"] = "keyword"
  list_mode:Literal[None, "entity", "property"] = None
  current_parent_node = None
  nodes_dict = {}
  start_ID = 0
  ID_generator = unique_value_generator(start_ID)

  layout = [
    [
      sg.Frame("graph", [[sg.Image("white.png", key=ImgKey, size=(700, 500))]]),
      sg.Frame("operate", [
        [sg.Text("キーワードを入力してください：", key=InduceSearchTextKey), sg.InputText(size=(20,1), key=SearchBoxKey), sg.Button("検索", key=DoSearchKey)],
        [sg.Text("概要：", key=AbstTitleKey)],
        [sg.Text("", key=AbstTextKey)],
        [sg.Text("", key=ErrorTextKey)],
        [sg.Text("検索結果", key=ListBoxTitle), sg.Button("決定", key=ChoiceFromListKey)],
        [sg.Listbox([], size=(30, 30), key=ListBoxKey)]
      ])
    ],
  ]

  window = sg.Window("深化型学習支援システム", layout, resizable=True, size=(1200,600))

  # event loop
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
      break
    if event == DoSearchKey:
      if search_mode == "keyword":
        keyword = values[SearchBoxKey]
        window[SearchBoxKey].update("")
        result_entities = do_inquiry(quereis.create_query_for_get_object_from_keyword(keyword))
        result_entities = reshapeResults.reshape_for_object(result_entities)
        if not result_entities:
          window[ErrorTextKey].update("検索結果がありません.",text_color="#FFFFFF", background_color="#FF0000")
          continue
        window[ErrorTextKey].update("", background_color="#64778D")
        window[ListBoxKey].update(["["+str(i)+"]"+str(result_entities[i]["label"]) for i in range(len(result_entities))])
        list_mode = "entity"
        search_mode = "ID"
        window[InduceSearchTextKey].update("IDを入力してください\n(リテラルは選択不可)")
      elif search_mode == "ID":
        choise_ID = int(unicodedata.normalize('NFKC', values[SearchBoxKey]))
        window[SearchBoxKey].update("")
        if manipulate_tree.find_node_by_ID(nodes_dict[start_ID], choise_ID) == -1:
          window[ErrorTextKey].update("ID値が不正です.", text_color="#FFFFFF", background_color="#FF0000")
          continue
        window[ErrorTextKey].update("", background_color="#64778D")
        current_parent_node = nodes_dict[choise_ID]
        if current_parent_node.node_type == "entity":
          window[ErrorTextKey].update("", background_color="#64778D")
          abstract = reshapeResults.reshape_for_abst(
            do_inquiry(quereis.create_query_for_get_abst_from_object(objectURI=current_parent_node.URI))
          )
          window[AbstTitleKey].update("概要：")
          window[AbstTextKey].update(abstract)
          result_property = do_inquiry(
            quereis.create_query_for_get_property_from_object(objectURI=current_parent_node.URI)
          )
          result_property = reshapeResults.reshape_for_property(result_property)
          window[ListBoxTitle].update("プロパティ一覧")
          window[ListBoxKey].update(["["+str(i)+"]"+str(result_property[i]["label"]) for i in range(len(result_property))])
          list_mode = "property"
        elif current_parent_node.node_type == "property":
          window[ErrorTextKey].update("", background_color="#64778D")
          result_entities = do_inquiry(
            quereis.create_query_for_get_object_from_set_of_entity_and_property(
              objectURI=current_parent_node.parent.URI, propertyURI=current_parent_node.URI)
          )
          result_entities = reshapeResults.reshape_for_object(result_entities)
          window[ListBoxTitle].update("エンティティ一覧")
          window[ListBoxKey].update(["["+str(i)+"]"+str(result_entities[i]["label"]) for i in range(len(result_entities))])
          list_mode = "entity"
        else:
          window[ErrorTextKey].update("選択ノードはリテラルです.リテラルは選択できません.", text_color="#FFFFFF", background_color="#FF0000")
    if event == ChoiceFromListKey:
      choise_ID = myfunc.extract_first_number(values[ListBoxKey][0])
      if list_mode == "entity":
        window[ListBoxKey].update([])
        if result_entities[choise_ID]["type"] == "entity":
          result_property = do_inquiry(quereis.create_query_for_get_property_from_object(objectURI=result_entities[choise_ID]["URI"]))
          result_property = reshapeResults.reshape_for_property(result_property)
          if not result_property:
            window[ErrorTextKey].update("そのエンティティはプロパティを持っていません", text_color="#FFFFFF", background_color="#FF0000")
            continue
          window[ErrorTextKey].update("", background_color="#64778D")
          node_ID = next(ID_generator)
          nodes_dict[node_ID] = manipulate_tree.create_node(
            name=result_entities[choise_ID]["label"],
            node_ID=node_ID,
            URI=result_entities[choise_ID]["URI"],
            node_type=result_entities[choise_ID]["type"],
            parent_node=current_parent_node
          )
          current_parent_node = nodes_dict[node_ID]
          abstract = reshapeResults.reshape_for_abst(do_inquiry(quereis.create_query_for_get_abst_from_object(objectURI=nodes_dict[node_ID].URI)))
          window[AbstTextKey].update(abstract)
          window[ListBoxTitle].update("プロパティ一覧")
          window[ListBoxKey].update(["["+str(i)+"]"+str(result_property[i]["label"]) for i in range(len(result_property))])
          list_mode = "property"
        elif result_entities[choise_ID]["type"] == "literal":
          node_ID = next(ID_generator)
          nodes_dict[node_ID] = manipulate_tree.create_node(
            name=result_entities[choise_ID]["label"],
            node_ID=node_ID,
            URI=None,
            node_type="literal",
            parent_node=current_parent_node
          )
          window[AbstTitleKey].update("リテラル値：")
          window[AbstTextKey].update(nodes_dict[node_ID].name)
          window[ListBoxKey].update([])
          list_mode = None
        if node_ID <= 1:
            continue
        manipulate_graph.renew_graph_pic(nodes_dict[start_ID])
        window[ImgKey].update("graph.png")
      elif list_mode == "property":
        result_entities = do_inquiry(
          quereis.create_query_for_get_object_from_set_of_entity_and_property(
            objectURI=current_parent_node.URI, propertyURI=result_property[choise_ID]["URI"]
          )
        )
        result_entities = reshapeResults.reshape_for_object(result_entities)
        if not result_entities:
          window[ErrorTextKey].update("そのプロパティはエンティティを持っていません.",text_color="#FFFFFF", background_color="#FF0000")
          continue
        window[ErrorTextKey].update("", background_color="#64778D")
        node_ID = next(ID_generator)
        nodes_dict[node_ID] = manipulate_tree.create_node(
          name=result_property[choise_ID]["label"],
          node_ID=node_ID,
          URI=result_property[choise_ID]["URI"],
          node_type="property",
          parent_node=current_parent_node
        )
        current_parent_node = nodes_dict[node_ID]
        window[ListBoxTitle].update("エンティティ一覧")
        window[ListBoxKey].update(["["+str(i)+"]"+str(result_entities[i]["label"]) for i in range(len(result_entities))])
        list_mode = "entity"


  window.close()

if __name__ == "__main__":
  main()