
import json
from pprint import pprint

prediction_list = [{'score': 0.71, 'attribute_code': '02419', 'label': '41852'}, 
                   {'score': 1.0, 'attribute_code': '15344', 'label': '00002'}, 
                   {'score': 0.98, 'attribute_code': '01746', 'label': '04214'}, 
                   {'score': 0.22, 'attribute_code': '00562', 'label': '01495'}, 
                   {'score': 0.3, 'attribute_code': '99999', 'label': '202372'}]

# for pred in prediction_list:
#     print(pred['attribute_code'])
#     print(pred['label'])
#     print(pred['score'])



prediction_list_text = "[{'score': 0.9, 'attribute_code': '02419', 'label': '00533'}, {'score': 1.0, 'attribute_code': '15344', 'label': '00002'}, {'score': 0.86, 'attribute_code': '01746', 'label': '01875'}, {'score': 0.92, 'attribute_code': '00562', 'label': '00900'}, {'score': 0.44, 'attribute_code': '99999', 'label': '200302'}]"

# print(prediction_list_text.replace('[', "").replace(']', ""))

prediction_list_json = json.dumps(prediction_list)

prediction_list_json2 = json.dumps(prediction_list_text)

print(type(prediction_list_json2))

testing = json.loads(prediction_list_json2)

for test_single in testing:
    print (test_single)