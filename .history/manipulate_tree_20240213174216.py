from anytree import Node, RenderTree
from typing import 
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal

def create_node(name:str, node_ID:int, URI:Literal[str, None]) -> Node: