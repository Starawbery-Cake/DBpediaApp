import quereis
import reshapeResults

result = quereis.do_inquiry(quereis.create_query_for_get_object_from_keyword("東京都"))

print(result)

reshape_result = []

for i in range(len(result["results"]["bindings"])):
  URI:str = result["results"]["bindings"][i]["object"]["value"]
  if URI.startswith("http://ja.dbpedia.org/resource/"):
    label = URI
    reshape_result.append({"type":"entity", "URI":URI, "label":URI.replace("http://ja.dbpedia.org/resource/", "")})

print(reshape_result)

print("-"*50)
print(["["+str(i)+"]"+str(reshape_result[i]["label"]) for i in range(len(reshape_result))])


print("-"*50)

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
is_URI_apended:bool = False
for i in range(len(result["results"]["bindings"])):
  is_URI_apended = True
  URI:str = result["results"]["bindings"][i]["property"]["value"]
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
print("-"*50)
for i in range(len(reshape_result)):
  print(reshape_result[i]["label"])

result = quereis.do_inquiry(quereis.create_query_for_get_object_from_set_of_entity_and_property(objectURI="http://ja.dbpedia.org/resource/東京都", propertyURI="http://ja.dbpedia.org/property/木"))
print(result)
reshape_result = reshapeResults.reshape_for_object(result)
print(reshape_result)