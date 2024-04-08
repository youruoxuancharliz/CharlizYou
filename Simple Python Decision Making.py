import random
allmovies = ["Top Gun Maverick", "The Social Network", "Spider-Man", "Glass Onion", "Enola Holmes"]
allseries = ["Brooklyn 99", "Suits", "Young Sheldon", "Superstore"]
countries = ["korea", 'hangzhou', 'japan', 'austrailia', 'taiwan']

print("Making your decisions.....")

me = input("choosing between movie and series, or countries?")

#include quotation marks 

if me == "countries" :
    print( countries[random.randint(0,4)] )
    print("This country is chosen.")

elif me == "movie and series" or 'movie and series' :
     x = input('OK, do you want to watch a movie or series today?')
     if x == 'series' :
         print( allseries[random.randint(0,3)])
         print('This series is chosen.')
     elif x == 'movie' or 'movies' :
          print( allmovies[random.randint(0,4)])
          print("This movie is chosen.")
     else : print("choose an option.")

else : print('choose an option')
    
    
