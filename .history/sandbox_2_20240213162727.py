import quereis

result = quereis.do_inquiry(quereis.create_query_for_get_object_from_keyword("東京都"))

print(result)

reshape_result = []

for item in result:
  reshape_result