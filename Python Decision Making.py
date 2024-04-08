import random
allmovies = ["Top Gun Maverick", "The Social Network", "Spider-Man", "Glass Onion", "Enola Holmes"]
allseries = ["Brooklyn 99", "Suits", "Young Sheldon", "Superstore"]

print("Making your decisions.....")
me = input("movie or series?")
#include quotation marks 

if me == "series":
    print( allseries[random.randint(0,3)])
    print( "This series is chosen.")
elif me == "movie" or "movies" :
     print( allmovies[random.randint(0,4)])
     print( "This movie is chosen.")
else : 
      print("choose an option.")
