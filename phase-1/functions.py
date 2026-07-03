# name = "Muzammil"
# name1 = "Ahmed"
# name2 = "Ibrahim"

# print(f"Hello {name}")
# print(f"Hello {name1}")
# print(f"Hello {name2}")

# Functions -> We use to put our repitive code in the functions and to easily break down the code


def greet(name, age=18):
    print(f"Hello {name}, your age is {age}")


name = input("Enter your name: ")
age = input("Enter your age: ")

greet(age=int(age), name=name)

# greet("Muzammil", 12)
# greet("Ahmed", 15)
# greet(name="Ibrahim")
