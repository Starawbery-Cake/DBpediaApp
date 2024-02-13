from typing import Dict, List


def reshape_for_object(raw_result:dict) -> List[Dict[str, Union[str]]:
  reshape_result = []

  for i in range(len(raw_result["results"]["bindings"])):
    URI:str = raw_result["results"]["bindings"][i]["object"]["value"]
    item_type = raw_result["results"]["bindings"][i]["object"]["type"]
    if URI.startswith("http://ja.dbpedia.org/resource/"):
      label = URI.replace("http://ja.dbpedia.org/resource/", "")
      reshape_result.append({"type":"entity", "URI":URI, "label":label})
    if item_type == "typed-literal" or item_type == "literal":
      value = raw_result["results"]["bindings"][i]["object"]["value"]
      reshape_result.append({"type":"literal", "value":value})

  return reshape_result


def reshape_for_abst(raw_result:dict) -> str:
  abst:str = raw_result["results"]["bindings"][0]["abst"]["value"]

  period_index = abst.find("。")
  if period_index != -1:
    abst = abst[:period_index+1] + "...(以下省略)"

  return abst

def reshape_for_property(raw_result:dict) -> List[Dict[str, str]]:
  reshape_result = []
  is_URI_apended:bool = False
  for i in range(len(raw_result["results"]["bindings"])):
    is_URI_apended = True
    URI:str = raw_result["results"]["bindings"][i]["property"]["value"]
    if URI.startswith("http://ja.dbpedia.org/property/"):
      label:str = URI.replace("http://ja.dbpedia.org/property/", "")
      if not reshape_result:
        reshape_result.append({"type":"property", "URI":URI, "label":label})
      else:
        for item in reshape_result:
        # for knownURI in reshape_result["URI"]:
          if item["URI"] != URI:
            is_URI_apended = False
            break
      if not is_URI_apended:
        reshape_result.append({"type":"property", "URI":URI, "label":label})
  return reshape_result