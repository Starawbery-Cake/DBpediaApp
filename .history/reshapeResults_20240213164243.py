def reshape_for_object(raw_result:dict) -> str:
  reshape_result = []

for i in range(len(result["results"]["bindings"])):
  URI:str = result["results"]["bindings"][i]["URI"]["value"]
  if URI.startswith("http://ja.dbpedia.org/resource/"):
    label = URI
    reshape_result.append({"type":"entity", "URI":URI, "label":URI.replace("http://ja.dbpedia.org/resource/", "")})