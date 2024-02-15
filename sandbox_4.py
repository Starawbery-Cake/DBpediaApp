import matplotlib.pyplot as plt
import networkx as nx
from manipulate_graph import hierarchy_pos

Graph = nx.DiGraph()

Graph.add_node("root", URI="http://root")
Graph.add_node("child", URI="http://child")
# Graph.add_node("child", URI="http://child2")

Graph.add_edge("root", "child", label="prop", URI="http://prop")
Graph.add_edge("child", "root", lable="prop", URI="http://prop")

# pos = hierarchy_pos(Graph, "root")
pos = nx.spring_layout(Graph)
edge_labels = nx.get_edge_attributes(Graph, 'label')
nx.draw(Graph, pos, with_labels=True, data=True, node_size=700, node_color="skyblue", font_family="BIZ UDGothic", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels, font_family="BIZ UDGothic")
plt.plot()
plt.show()