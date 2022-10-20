d = {"topping": [
                 {"id": 5002, "type": "glazed"},
                 {"id": 5003, "type": "chocolate"},
                 {"id": 5004, "type": "maple"}
                ]
    }

for keys, values in d.items():
    print("Keys:", keys)
    print("Values:", values)
    for value in values:
        if value["type"] == "chocolate":
            print("id:", value["id"])
