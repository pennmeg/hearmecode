## --- 2: Lists and Loops

attendees = ["Joe", "Jane", "John"]
# print(len(attendees))

# attendees.append("Jill") # Adding 1
# print(attendees)
# print(len(attendees))

# name = attendees.pop(2) # Removing
# print(name)

# attendees.extend(["June", "Jack"]) # Adding more than one
# print(attendees)

# attendees.insert(0, "Annie") # Adds one in a specific index
# print(attendees)

# address = "123 Main Street"
# list = address.split(" ")
# print(list)

# print("123" in address)
# print("124" in list)

# for name in attendees:
#     print(name)

# for index, name in enumerate(attendees): # Adds a counter to an iterable object
#     print(index, name)

# * Can also do nested loops 

# for n in range(5): # list of Numbers
#     print(n)

# range(start, stop, step)
# for week in range(1,4):
#     print("Week {0}".format(week))

# provinces = ["Ontario", "Alberta", "Quebec"]
# provinces_abbr = ["ON", "AB", "PQ"]

# for abbr, name in zip(provinces_abbr, provinces):
#     print("Short name for {0} is {1}".format(name, abbr))

count = 5

while count >= 0:
    print("Let's count", count)
    count = count - 1

