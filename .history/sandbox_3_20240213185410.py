import quereis
import reshapeResults

result = quereis.do_inquiry(quereis.create_query_for_get_object_from_keyword("東京都"))
result = reshapeResults.reshape_for_object(result)

print(result[0]["type"])