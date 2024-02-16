import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from anytree import Node


def search_graph(root_node:Node, Graph:nx.DiGraph) -> int:
  children = root_node.children
  for child in children:
    search_graph(child, Graph)
  if root_node.parent == None:
    return 0
  if root_node.node_type != "property":
    node_type_tag = {"entity":"E", "literal":"L"}
    Graph.add_edge(
      ( node_type_tag[root_node.parent.parent.node_type] + ":" + \
        root_node.parent.parent.name + "(ID=" + str(root_node.parent.parent.node_ID) + ")"),
      ( node_type_tag[root_node.node_type] + ":" + \
        root_node.name + "(ID=" + str(root_node.node_ID) + ")"),
      label=("P:" + root_node.parent.name + "(ID=" + str(root_node.parent.node_ID) + ")")
    )


def renew_graph_pic(root_node:Node) -> nx.DiGraph:
  font = "Noto Sans CJK JP"
  Graph = nx.DiGraph()
  search_graph(root_node, Graph)
  pos = hierarchy_pos(Graph, ("E:" + root_node.name+"(ID="+str(root_node.node_ID)+")"))
  edge_labels = nx.get_edge_attributes(Graph, 'label')
  nx.draw(Graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_family="BIZ UDGothic", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
  nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels, font_family="BIZ UDGothic")
  plt.plot()
  plt.savefig("graph.png", format="png")
  plt.show()


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
  '''
  ツリーまたは森の階層的レイアウトを生成する。

  :param G: networkxのグラフ
  :param root: ルートノード。Noneの場合は全ノードから自動的にルートを決定
  :param width: 横方向のスケール
  :param vert_gap: 階層間の垂直間隔
  :param vert_loc: ルートノードの垂直位置
  :param xcenter: グラフの中心の横位置
  :return: ノードと位置の辞書
  '''
  if not nx.is_tree(G):
    raise TypeError('木構造ではありません')

  if root is None:
    if isinstance(G, nx.DiGraph):
      root = next(iter(nx.topological_sort(G)))  # ルートを決定するためのトポロジカルソート
    else:
      root = 0  # 最初のノードをルートとして使用

  def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
      if pos is None:
        pos = {root: (xcenter, vert_loc)}
      else:
        pos[root] = (xcenter, vert_loc)
      children = list(G.neighbors(root))
      if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)
      if len(children) != 0:
        dx = width / 2
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
          nextx += dx
          pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
      return pos

  return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)