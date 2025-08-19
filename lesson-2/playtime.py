## --- 99 Bottles

# bottle = 99

# while bottle > 0:
#     print("{0} bottles of beer on the wall, {0} bottles of beer... \n If one of those bottles should happen to fall {1} bottles of beer on the wall.".format(bottle, bottle-1))
#     bottle = bottle - 1

## --- Fibonnaci Sequence

sequence = [0, 1]
while len(sequence) < 11:
    sequence.append(sequence[-1] + sequence[-2])

# print(sequence)

## --- FizzBuzz

# When you land on a number evenly divisible by 3, have your program print "Fizz"
# When you land on a number evenly divisible by 5, have your program print "Buzz"
# When you land on a number evenly divisible by both 3 and 5, have your program print "Fizzbuzz"
# When you land on any other number, print that number

# for num in range (1,101):
#     if num % 5 == 0 and num % 3 == 0:
#         print("Fizzbuzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print(num)

## --- CSV

movie_titles = [
    "Everything Everywhere All at Once",
    "The Dark Knight",
    "Barbie",
    "Inception",
    "Lady Bird"
]

parental_rating = [
    "R",       
    "PG-13",   
    "PG-13",   
    "PG-13",   
    "R"       
]

bechdel_rating = [
    3,  
    1,  
    3, 
    1,  
    3   
]

imdb_rating = [
    7.9,  
    9.0,  
    7.0,  
    8.8, 
    7.4   
]

genre = [
    "Sci-Fi/Adventure",
    "Action/Crime",
    "Comedy/Fantasy",
    "Sci-Fi/Thriller",
    "Drama/Coming-of-age"
]


# for mt, pr, br, ir, g in zip(movie_titles, parental_rating, bechdel_rating, imdb_rating, genre):
#     print(mt, pr, br, ir, g, sep=", ")


## TO DO:
## --- States

## --- PB