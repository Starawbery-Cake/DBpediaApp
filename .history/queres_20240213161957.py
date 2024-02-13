from SPARQLWrapper import SPARQLWrapper, JSON
try:
  from typing import Literal
except ImportError:
  from typing_extensions import Literal


def create_query_for_get_abst_from_object(objectURI:str) ->str:
  query = """
  SELECT DISTINCT ?abst
  WHERE
  {
    <""" + objectURI + """> dbo:abstract ?abst .
  }
  """

  return query


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

  return query


def create_query_for_get_property_from_object(objectURI:str) ->str:
  query = """
  SELECT DISTINCT ?property
  WHERE
  {
    <""" + objectURI + """> ?property ?object .
  }
  """

  return query


def create_query_for_get_object_from_set_of_entity_and_property(objectURI:str, propertyURI:str) ->str:
  query = """
  SELECT DISTINCT ?object
  WHERE
  {
    <""" + objectURI + """> <""" + propertyURI +  """> ?object .
  }
  """

  return query

def do_inquiry(query:str) -> dict:
  sparqlDBpedia = SPARQLWrapper("https://ja.dbpedia.org/sparql", returnFormat="json")
  sparqlDBpedia.setReturnFormat(JSON)