import time

# Modes related to files

# Read -> Content reading (r)
# Write -> Content writting (w)
# Append -> Content append (a)

# file = open("context.txt", "r")
# print(file.read())
# single_line = file.readline()
# print(single_line[0:3])
# print(type(single_line))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# file = open("context.txt", "w")
# file.write("Hello World")

# file = open("context.txt", "a")
# file.write("Hello World\n")

# print(100 / 0)

# try:
#     file = open("contexts.txt")
#     print(file.read())

#     numb = int(input("Enter a number: "))
#     print(numb / 0)
# except FileNotFoundError as e:
#     print("File not found: {e}")
# # file not found: {e}
# # file not found: [Errno 2] No such file or directory: 'contexts.txt'
# except ZeroDivisionError as e:
#     print(f"Sorry! {e}")

# Open -> Operation -> Close
# RAM -> Consume
# SaaS ->

# Context Manager

# with open("context.txt") as file:
#     time.sleep(10)
#     print(file.read())
