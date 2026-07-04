# students = ["Muzammil", "Ahmed", "Khan"]

# Dictionary -> Key - Value Pairs

info = {
  "name":"Muzammil",
  "age":20,
  "class": "2nd Year",
  "hobbies":"Coding"
}
# print(info["name"])
# print(info["age"])

# for key, value in info.items():
#   print(key)

students = [
  {"name":"Muzammil", "age": 21},
  {"name":"Ahmed", "age": 25},
  {"name":"Nadeem", "age": 24},
]

for student in students:
  for key, value in student.items():
    print(key, value)
