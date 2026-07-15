# name1 = "Muzammil"
# name2 = "Ahmed"
# name3 = "Nadeem"

# numbers = [1, 2, 3, 4, 5, 6]

# names = ["Muzammil", "Ahmed", "Nadeem"]
# print(names)
# print(names[0])
# names.pop(0)
# print(names)

# muzammilName = "Muzammil"
# muzammilAge = 19
# muzammilHobby = "Coding"

# muzammilInfo = {"name": "Muzmamil", "age": 19, "hobby": "Coding"}
# ahmedInfo = {"name": "Muzmamil", "age": 19, "hobby": "Coding"}
# nadeemInfo = {"name": "Nadeem", "age": 19, "hobby": "Coding"}

# Immutable -> Memory Effect  -> Tuples
# Mutable -> Lists

# names = [
#     {"name": "Muzmamil", "age": 19, "hobby": "Coding"},
#     {"name": "Ahmed", "age": 19, "hobby": "Coding"},
#     {"name": "Nadeem", "age": 19, "hobby": "Coding"},
# ]

# print(names)
# names.pop(1)
# print(names)

# names = ["Muzammil", "Ahmed", "Nadeem", "Ibrahim"]

# for index, name in enumerate(names, 1):
#     print(index, name)

# CRUD ->
# C -> Create
# R -> Read
# U -> Update
# D -> Delete

# Functions
# while loop
# Conditions
# Lists
# Dictionary


# First we created a list to store the tasks in the form of dictionary

tasks = [
    {"title": "Learn TypeScript", "completed": False},
    {"title": "Learn JavaScript", "completed": False},
]

# View Task function loops on the list and display the elemens (dictionary) one by one

# enumerate


def view_task():
    print("\n")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task["title"]} - {task["completed"]}")
    print("\n")


# Add Task function takes input from the user and appends in the list


def add_task():
    print("==== Enter the task which you want to add ====")
    task = input("Enter your task: ")
    tasks.append({"title": task, "completed": False})
    print("Your task has been added")


def delete_task():
    view_task()
    print("=== Enter the number to delete the task ===")
    index = int(input("Enter the number: "))
    print(f"You are going to remove {index}")
    tasks.pop(index - 1)
    view_task()


def task_completed():
    view_task()
    print("=== Enter the number to update the task ===")
    index = int(input("Enter the number: "))
    print(f"You are going to update {index}")
    tasks[index - 1]["completed"] = True
    # dict = tasks[index - 1]
    # dict["completed"] = True
    print("Your task has been updated")


# view_task()
# add_task()
# view_task()

# names = ["Muzammil", "Ahmed", "Nadeem", "Ibrahim"]
# print(names)
# names.pop(0)
# print(names)

while True:
    print("\n")
    print("=" * 50)
    print("Choose the operation: ")
    print("1. View Task")
    print("2. Create Task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Quit")
    print("=" * 50)
    print("\n")

    operation = input("Enter the number (1, 2, 3, 4 or 5): ")  # block
    print(f"You have chosen {operation}")

    if int(operation) == 1:
        view_task()
    elif int(operation) == 2:
        add_task()
    elif int(operation) == 3:
        delete_task()
    elif int(operation) == 4:
        task_completed()
    elif int(operation) == 5:
        print("You are going to exit the loop")
        break
    else:
        print("Invalid Operation")

# names = ["Muzammil", "Ahmed"]
# print("Before Update: ", names)  # Move lines up Alt + Up Arrow
# names[1] = "Nadeem"
# print("After Update: ", names)  # Move lines up Alt + Up Arrow

# names = [
#     {"name": "Muzammil", "age": 19},
#     {"name": "Ahmed", "age": 24},
# ]

# Not a best practice

# print(names)
# names[0] = {"name": "Nadeem", "age": 20}
# print(names)

# Best practice

# Dictionary -> Key - Value pairs

# dict = {"name": "Muzammil"}
# print(dict)
# dict["name"] = "Nadeem"
# print(dict)

# print(names)
# names[0]["name"] = "Nadeem"
# print(names)

# List [] -> Collection of data
# Dictionary {} -> Extra information in the form of keys and value

# In order to get particular elements from the list we have to use index
# For example:

# names = ["Muzammil", "Ahmed"]
# print(names[0])  # We have used 0 as the index to get the first element

# # Now in order to replace the first element (Muzammil -> Nadeem)
# names[0] = "Nadeem"  # We have updated the first element (Muzammil -> Nadeem)
# print(names[0])  # Nadeem

# # Dictionary -> Key - Value Pair
# student = {
#     "name": "Muzammil"
# }  # In order to create a dictionary we use "{}", here name is the key and Muzammil is the value

# In order to access the value of (key: name)
# print(
#     student["name"]
# )  # Muzammil, In order to get the value from a dictionary we use the key.

# Now if we need to update the dictionary we can do it like this
# student["name"] = "Nadeem"  # We have updated the value (Muzammil -> Nadeem)
# print(student["name"])  # Nadeem

# # In order to get the dictionary from the list
# names = [
#     {"name": "Muzammil", "age": 20},
# ]

# print("Accessing using index: ", names[0])
# print("Getting the name from the dict: ", names[0]["name"])
# names[0]["name"] = "Nadeem"
# print("Getting the name from the dict: (After update) ", names[0]["name"])
