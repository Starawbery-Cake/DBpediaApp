from SPARQLWrapper import SPARQLWrapper
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal

def create_query_for_get_