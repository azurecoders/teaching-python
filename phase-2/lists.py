# List is a datatype that holds the collection of data (of any datatype)

names = ["Muzammil", "Ahmed", "Nadeem"]
# numbers = [1,2,3,4,5,6,7,8,9]

def greet(name):
  print(f"Hello, {name}")

for name in names:
  greet(name)
# Indexes always starts from 0

# print(names[0]) # Start of the list
# print(names[2]) # End of the list
# print(names[-1]) # End of the list -> Reverse Order

# Slicing
# print(names[0:2])
# Last value always be deducted with -1

# print(numbers[1::3])
# print(names[-3:])

# print(numbers[0:5:2])
# start:stop:skip

# print(names)
# names.append("Ibrahim")
# names.extend(["Ibrahim", "Arshad"]) # prefered method
# print([1,2,3] + [4,5,6])
# names.insert(1, "Ibrahim")
# names.remove("Ahmed")
# print(names.pop())
# print(names.index("Muzammil"))
# print(names.count("Ahmed"))
# print(names)
