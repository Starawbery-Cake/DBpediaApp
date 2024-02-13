import anytree
from anytree import Node, RenderTree
import querys
from querys import do_inquiry
import manipulateNode
from reshapeInquiryData import reshape_entites_from_keyword


startID = 0

def unique_value_generator(start_value=startID):
    current_value = start_value
    while True:
        yield current_value
        current_value += 1

ID_generator = unique_value_generator()

nodes_dict = {}

# キーワード検索実行
print("input keyword here.")
# 検索結果取得
result = do_inquiry(querys.create_get_URIs_query(keyword="東京都"))
print("do inquiry here.")
# 検索結果整理
result = reshape_entites_from_keyword(result)
print("reshape result here.")
# 検索結果表示
print("show the result of search here.")
# 調査対象選択受付
selected_label = "東京都" # 本来は入力された値が存在するかチェックする]
print("choice a label here.")
# ルートノード設定：調査対象
node_ID = next(ID_generator)
nodes_dict[node_ID] = manipulateNode.create_node(
  node_type="entity",
  name=result[selected_number]["URILabel"]
)
print("set root node here.")


i = 0
repeat = 1
while i<repeat:
  pass
  # 調査対象abst表示
  print("print abstract here.")
  print(do_inquiry(querys.create_get_abst_query(subject_URI=current_pearent_node.URI))["results"]["bindings"][0]["abst"]["value"])
  # 調査対象プロパティ取得
  print("get property here.")
  propertes = do_inquiry(querys.create_get_propertes_query(subject_URI=current_pearent_node.URI))
  # プロパティ整理
  print("reshape propertes here.")
  propertes = reshape_label_result(propertes)
  # 対象プロパティ選択受付
  print("choice a property here.")
  selected_property = "http://purl.org/dc/terms/subject" # 本来は入力された値が存在するかチェックする.
  # プロパティノード追加：対象プロパティ
  node_ID = next(ID_generator)
  nodes_dict[node_ID] = Node(
    name="P:"+selected_property,
    parent=current_pearent_node,
    URI=selected_property,
    node_type="property",
    ID=node_ID
  )
  current_pearent_node = nodes_dict[node_ID]
  # プロパティに対応するオブジェクト一覧取得
  print(current_pearent_node.parent.URI, current_pearent_node.URI)
  result = do_inquiry(querys.create_get_objects_query(subject_URI=current_pearent_node.parent.URI, property_URI=current_pearent_node.URI))
  # オブジェクト整理
  result = reshape_keyword_result(result)
  # オブジェクト一覧表示
  print("show all objects here.")
  # オブジェクト選択入力受付
  print("choice a object here.")
  selected_object = "Category:日本の都道府県" # 本来は入力された値が存在するかチェックする.
  # オブジェクトノード追加
  node_ID = next(ID_generator)
  nodes_dict[node_ID] = Node(
    name="E:"+selected_object,
    parent=current_pearent_node,
    URI=result[selected_object],
    node_type="entity",
    ID=node_ID
  )
  i += 1

for pre, fill, node in RenderTree(nodes_dict[startID]):
  print(f"{pre}{node.name}(ID={node.ID})")