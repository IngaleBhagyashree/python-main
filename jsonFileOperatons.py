import json

json_string='''{ 
    "students":[
    {
        "name":"hii",
        "rollNo":111,
        "add":"wagholi"
    },
    {
        "name":"hello",
        "rollNo":112,
        "add":"gholi"
    }
    ]
} '''

data=json.loads(json_string)
print(data)

for student in data["students"]:
    print("Name:", student["name"])
    print("rollNo",student["rollNo"])
    print("address:",student["add"])