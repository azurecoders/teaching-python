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
    print("4. Quit")
    print("=" * 50)
    print("\n")

    operation = input("Enter the number (1, 2 or 3): ")  # block
    print(f"You have chosen {operation}")

    if int(operation) == 1:
        view_task()
    elif int(operation) == 2:
        add_task()
    elif int(operation) == 3:
        delete_task()
    elif int(operation) == 4:
        print("You are going to exit the loop")
        break
    else:
        print("Invalid Operation")
