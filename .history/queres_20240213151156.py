from SPARQLWrapper import SPARQLWrapper
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal

def create_query_for_get_object_from_keyword(keyword:str) ->str:
  query = """
  SELECT DISTINCT ?URI ?label
  WHERE
  {
    ?URI rdfs:label ?label .
    FILTER(?label = \"""" \
    + keyword + """\"@ja).
  }
  """