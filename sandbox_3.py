from manipulate_tree import create_node,show_the_tree
import networkx as nx
import matplotlib.pyplot as plt
import manipulate_graph

nodes_dict = {}

nodes_dict[0] = create_node(
  name="root_ルート", node_ID=0, URI=None, node_type="entity", parent_node=None
)

nodes_dict[1] = create_node(
  name="prop1_プロパティ1", node_ID=1, URI=None, node_type="property", parent_node=nodes_dict[0]
)

nodes_dict[2] = create_node(
  name="entity1-1", node_ID=2, URI=None, node_type="entity", parent_node=nodes_dict[1]
)

nodes_dict[3] = create_node(
  name="entity1-2", node_ID=3, URI=None, node_type="entity", parent_node=nodes_dict[1]
)

nodes_dict[4] = create_node(
  name="property2", node_ID=4, URI=None, node_type="property", parent_node=nodes_dict[0]
)

nodes_dict[5] = create_node(
  name="entity2-1", node_ID=5, URI=None, node_type="entity", parent_node=nodes_dict[4]
)

nodes_dict[6] = create_node(
  name="property1-1", node_ID=6, URI=None, node_type="property", parent_node=nodes_dict[2]
)

nodes_dict[7] = create_node(
  name="entity1-1-1", node_ID=7, URI=None, node_type="entity", parent_node=nodes_dict[6]
)

show_the_tree(nodes_dict[0])


def search_graph(current_node, Graph):
  print(current_node)
  children = current_node.children
  for child in children:
    search_graph(child, Graph)
  if current_node.parent == None:
    return 1
  if current_node.node_type != "property":
    Graph.add_edge(current_node.parent.parent.name, current_node.name, label=current_node.parent.name)

# search_graph(nodes_dict[0])

visualized_Graph = nx.DiGraph()
# search_graph(nodes_dict[0], visualized_Graph)
# manipulate_graph.renew_graph(nodes_dict[0], visualized_Graph)
# pos = nx.spring_layout(visualized_Graph)
# edge_labels = nx.get_edge_attributes(visualized_Graph, 'label')
# nx.draw(visualized_Graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
# nx.draw_networkx_edge_labels(visualized_Graph, pos, edge_labels=edge_labels)
# plt.show()
# plt.savefig("graph.png", format="PNG")
manipulate_graph.renew_graph_pic(nodes_dict[0])

nodes_dict[8] = create_node(
  name="property2-1", node_ID=8, URI=None, node_type="property", parent_node=nodes_dict[5]
)

nodes_dict[9] = create_node(
  name="literal2-1-1", node_ID=9, URI=None, node_type="literal", parent_node=nodes_dict[8]
)

manipulate_graph.renew_graph_pic(nodes_dict[0])


