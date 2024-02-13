import PySimpleGUI as sg
import quereis
from quereis import do_inquiry
import reshapeResults
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal


def main():
  ImgKey = "img"
  InduceSearchTextKey = "induce"
  SearchWordKey = "search_word"
  DoSearchKey = "do_search"
  AbstTextKey = "abst"
  ErrorTextKey = "error"
  ListBoxKey = "listBox"

  search_mode:Literal["keyword", "ID"] = "keyword"
  list_mode:Literal[None, "entity", "property"] = None

  layout = [
    [
      sg.Frame("graph", [[sg.Image("white.png", key=ImgKey)]]),
      sg.Frame("operate", [
        [sg.Text("キーワードを入力してください：", key=InduceSearchTextKey), sg.InputText(size=(20,1), key=SearchWordKey), sg.Button("検索", key=DoSearchKey)],
        [sg.Text("概要：")],
        [sg.Text("", key=AbstTextKey)],
        [sg.Text("", key=ErrorTextKey)],
        [sg.Text("検索結果"), sg.Button("決定")],
        [sg.Listbox([], size=(30, 30), key=ListBoxKey)]
      ])
    ],
  ]

  window = sg.Window("深化型学習支援システム", layout, resizable=True)

  # event loop
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
      break
    if event == DoSearchKey:
      if search_mode == "keyword":
        keyword = values[SearchWordKey]
        result_entities = do_inquiry(quereis.create_query_for_get_object_from_keyword(keyword))
        result_entities = reshapeResults.reshape_for_object(result_entities)
        if not result_entities:
          window[ErrorTextKey].update("検索結果がありません.",text_color="#FFFFFF", background_color="#FF0000")
          continue
        window[ErrorTextKey].update("", background_color="#64778D")
        window[ListBoxKey].update(["["+str(i)+"]"+str(result_entities[i]["label"]) for i in range(len(result_entities))])
        list_mode = "entity"
        search_mode = "ID"
    if event == li

  window.close()

if __name__ == "__main__":
  main()