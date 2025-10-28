# Dictionary --> {key: value}

student1 = {
    "id": 1, 
    "name": "Ravi", 
    "age": 23, 
    "Dept": "IT",
    "favColor": ["blue", "black", "red"],
    "address": {
        "Dno": "No2",
        "street": "XYZ"
    },
    "age": 35,
}

# print(student1)
# print(type(student1))
# print(student1["favColor"][1])
# print(student1.keys())
# print(student1.values())

# student1["hairColor"] = "Meroon"
# student1.update({"name": "RaviKumar"})

student1.pop("name")
student1.popitem()
student1.clear()

print(student1)