## --- 1: Strings and Conditionals
name = "Megan"
print(name)
## Strings
#  Use """ for multiline strings """
# Special Characters \n for newline and \t for tab
print("Lesson \t Topic \n 1 \t Strings and Conditionals \n 2 \t Lists and Loops")
print(len(name)) # Length
print(name[0]) # Slice
print(name[1:3])
print(name[:3])
print(name[3:])
phone = "000-123-4567"
print("Call {0} for a great pizza".format(phone[4:]))
print("Call ({0}) {1} for a great pizza".format(phone[0:3],phone[4:]))
print(name.find("1")) # Find: Not Found
print(name.find("n")) # Find
print(phone.replace('0', '9')) # Replace
address = "   123      Main St   "
print(address)
print(address.strip()) # Strip
print(name.upper()) # Upper
print(name.lower()) # Lower
print(phone.count("0")) # Count

# Conditionals
print(5 == 5) # Equality
print(5 == 7)
print(5 > 7) # Greater Than
print(5 > 2)
# != Not Equal
# < Less Than
# >= Great Than Equal To
# <= Less Than Equal To

students = 10
capacity = 50
ta = 5

if students < capacity:
    print("Keep Recruiting")
else: 
    print("Class Full")

if ta == 0:
    print("Uh oh!")
elif ta < students / 5:
    print("Need more TAs")
else:
    print("TAs are great!")

if "Hear Me Code" in "Hear Me Code is more than...":
    print("yay")
else:
    print("no")

# Compound Conditionals "and" "or"