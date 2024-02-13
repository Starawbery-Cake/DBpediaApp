from anytree import Node, RenderTree
from typing import Union
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal

def create_node(name:str, node_ID:int, URI:Union[str, None], node_type:Literal["entity", "property", "literal"], parent_node:Union[None, Node]) -> Node:
  node = Node(name=name, ID=node_ID, URI=URI, node_type=node_type, pare)