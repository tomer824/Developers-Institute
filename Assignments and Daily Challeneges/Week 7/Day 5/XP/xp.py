import json

# sampleJson = { 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }

# print(sampleJson["company"]["employee"]["payble"]["salary"])


sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

# Expected Output:

{
    "age": 29,
    "id": 1,
    "name": "value2"
}

sorted_dict = dict(sorted(sampleJson.items()))
json_file = "index.json"

with open(json_file, "w") as f:
    json.dump(sorted_dict, f)
