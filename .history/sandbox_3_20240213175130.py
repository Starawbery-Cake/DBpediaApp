from manipulate_tree import create_node

nodes_dict = []
nodes_dict[0] = create_node(name="root", node_ID=0, URI=None, node_type="entity", parent_node=None)
nodes_dict[1] = create_node(name="chiled1", node_ID=1, URI=None, node_type="property", parent_node=nodes_dict[0])

