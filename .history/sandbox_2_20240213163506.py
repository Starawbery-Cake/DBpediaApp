import quereis

result = quereis.do_inquiry(quereis.create_query_for_get_object_from_keyword("東京都"))

print(result)

reshape_result = []

for i in len(result["head"]["results"]):
  URI:str = result["head"]["results"][i]["URI"]["value"]
  if URI.startswith("http://ja.dbpedia.org/resource/"):
    label = URI
    reshape_result.append({"type":"entity", "URI":URI, "label":URI.replace("http://ja.dbpedia.org/resource/", "")})

print()
