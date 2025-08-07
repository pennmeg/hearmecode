# ----------- Peanut Butter Jelly Time!

# -- To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

# breadSlices = 2
# peanutButter = 1
# jelly = 1 

# if breadSlices >= 2 and peanutButter >= 1 and jelly >= 1:
#     print("I can make a PB&J")
# else:
#     print("Looks like I dont' have enough for a PB&J")

# -- To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before
#   To calculate which ingredient you have the least of, the min() function will be useful.
#   min() will calculate the smallest number of all of the numbers in the parentheses and tell you which it is
#   For example, min(4, 83, 6) will return 4


# breadSlices = 4
# peanutButter = 2
# jelly = 2

# if breadSlices >= 2 and peanutButter >= 1 and jelly >= 1:
#     maxSandwiches = min(breadSlices // 2, peanutButter, jelly)
#     print("I can make this many sandwiches:", maxSandwiches)
# else:
#     print("Looks like I dont' have enough for a PB&J")

# -- To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py

# breadSlices = 3
# peanutButter = 2
# jelly = 2

# if breadSlices >= 2 and peanutButter >= 1 and jelly >= 1:
#     full = min(breadSlices // 2, peanutButter, jelly)
#     print("I can make this many sandwiches:", full)

#     openBread = breadSlices - (full * 2)
#     openPeanutButter = peanutButter - full
#     openJelly = jelly - full

#     if openBread >= 1 and openPeanutButter >= 1 and openJelly >= 1:
#         print("I can also make an open-face sandwich.")
# else:
#     print("Looks like I dont' have enough for a PB&J")

# -- To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches


# breadSlices = 3
# peanutButter = 2
# jelly = 0

# if breadSlices >= 2 and peanutButter >= 1 and jelly >= 1:
#     full = min(breadSlices // 2, peanutButter, jelly)
#     print("I can make this many sandwiches:", full)

#     openBread = breadSlices - (full * 2)
#     openPeanutButter = peanutButter - full
#     openJelly = jelly - full

#     if openBread >= 1 and openPeanutButter >= 1 and openJelly >= 1:
#         print("I can also make an open-face sandwich.")
# elif breadSlices >= 2 and peanutButter >= 1:
#     print("I can make only a PB")
# else:
#     print("Looks like I dont' have enough for a PB&J")

# -- To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

# breadSlices = 3
# peanutButter = 0
# jelly = 0

# if breadSlices >= 2 and peanutButter >= 1 and jelly >= 1:
#     full = min(breadSlices // 2, peanutButter, jelly)
#     print("I can make this many sandwiches:", full)

#     openBread = breadSlices - (full * 2)
#     openPeanutButter = peanutButter - full
#     openJelly = jelly - full

#     if openBread >= 1 and openPeanutButter >= 1 and openJelly >= 1:
#         print("I can also make an open-face sandwich.")
# elif breadSlices >= 2 and peanutButter >= 1:
#     print("I can make only a PB")
# else:
#     # print("Looks like I dont' have enough for a PB&J")
#     if breadSlices <= 2:
#         print("I'm missing bread")
#     if jelly <= 1:
#         print("i'm missing jelly")
#     if peanutButter <= 1:
#         print("I'm missing PB")

# ----------- Tweet length calculator

tweet = "It's Thursday; also known as Friday-eve. It's almost Friday! Here's some more letters to try to get above 140."
tweetLength = len(tweet)

# -- Measure the length of a tweet. Is it more than 140 characters?

# if tweetLength > 140:
#     print("Tweet is too long")
# else:
#     print("What a witty tweet")

# -- How many characters are left?

# maxLength = 140
# remainingChar = maxLength - tweetLength

# if remainingChar <= 0:
#     print("There are 0 characters remaining.")
# else:
#     print("Number of characters remaining:", remainingChar)


# -- Make the limit flexible


maxLength = 280

if tweetLength > maxLength:
    print("Tweet is too long")
else:
    print("What a witty tweet")
