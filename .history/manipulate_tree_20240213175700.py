from anytree import Node, RenderTree
from typing import Union
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal


def create_node(name:str, node_ID:int, URI:Union[str, None], node_type:Literal["entity", "property", "literal"], parent_node:Union[None, Node]) -> Node:
  node = Node(name=name, node_ID=node_ID, URI=URI, node_type=node_type, parent=parent_node)
  return node


def find_node_by_ID()


def show_the_tree(root_node:Node):
  for pre, fill, node in RenderTree(root_node):
    if node.node_type == "entity":
      print(f"{pre}E:{node.name}(ID={node.node_ID})")
    elif node.node_type == "property":
      print(f"{pre}P:{node.name}(ID={node.node_ID})")
    elif node.node_type == "literal":
      print(f"{pre}L:{node.name}(ID={node.node_ID})")