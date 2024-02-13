import quereis

result = quereis.do_inquiry(quereis.create_query_for_get_object_from_keyword("東京都"))

print(result)

reshape_result = []

for i in range(len(result["results"]["bindings"])):
  URI:str = result["results"]["bindings"][i]["object"]["value"]
  if URI.startswith("http://ja.dbpedia.org/resource/"):
    label = URI
    reshape_result.append({"type":"entity", "URI":URI, "label":URI.replace("http://ja.dbpedia.org/resource/", "")})

print(reshape_result)

result = quereis.do_inquiry(quereis.create_query_for_get_abst_from_object(objectURI="http://ja.dbpedia.org/resource/東京都"))
print(result)

abst:str = result["results"]["bindings"][0]["abst"]["value"]

period_index = abst.find("。")
if period_index != -1:
  abst = abst[:period_index+1] + "...(以下省略)"
print(abst)

result = quereis.do_inquiry(quereis.create_query_for_get_property_from_object(objectURI="http://ja.dbpedia.org/resource/東京都"))
print(result)

reshape_result = []
for i in range(len(result["results"]["bindings"])):
  URI:str = result["results"]["bindings"][i]["property"]["value"]
  if URI.startswith("http://ja.dbpedia.org/property/"):
    if not reshape_result:

    