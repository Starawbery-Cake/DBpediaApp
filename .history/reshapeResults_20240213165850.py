from typing import Dict, List


def reshape_for_object(raw_result:dict) -> List[Dict[str, str]]:
  reshape_result = []

  for i in range(len(raw_result["results"]["bindings"])):
    URI:str = raw_result["results"]["bindings"][i]["object"]["value"]
    if URI.startswith("http://ja.dbpedia.org/resource/"):
      label = URI.replace("http://ja.dbpedia.org/resource/", "")
      reshape_result.append({"type":"entity", "URI":URI, "label":label})

  return reshape_result


def reshape_for_abst(raw_result:dict) -> str:
  abst:str = raw_result["results"]["bindings"][0]["abst"]["value"]

  period_index = abst.find("。")
  if period_index != -1:
    abst = abst[:period_index+1] + "...(以下省略)"

  return abst