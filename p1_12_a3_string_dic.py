#  What is a Dictionary?

# Dictionary (dict) ek collection hota hai jo key-value pairs me data store karta hai.


student = {
    "name": "Nishant",
    "age": 20,
    "course": "Data Analyst"
}
#  Accessing Values
print(student["name"])   # Nishant
print(student.get("age"))  # 20
#  Add / Update Data
student["city"] = "Bhopal"   # Add
student["age"] = 21          # Update

print(student)
#  Remove Data
student.pop("age")   # remove key
del student["city"]  # delete

print(student)
#  Loop in Dictionary
for key, value in student.items():
    print(key, value)
#  Important Dictionary Methods
print(student.keys())    # all keys
print(student.values())  # all values
print(student.items())   # key-value pairs
#  Nested Dictionary
data = {
    "student1": {"name": "Nishant", "age": 20},
    "student2": {"name": "Rahul", "age": 22}
}

print(data["student1"]["name"])