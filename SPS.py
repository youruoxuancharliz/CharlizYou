import random
options = ( "rock", "paper", "scissors")
print( "The Game of Scissors Paper Stone")
computer = options[random.randint(0,2)]
print( "Hi, Introduce yourself! Whats your name?" )
x = input()
print( "Welcome to the game," + x + "!")
player= input("Choose Rock, Paper or Scissors?")

 #Remember to add indents when needed. Tabs are preferred.
#Remember to add " : "

 if player.lower == computer :
  print( "Its a tie! Try again." )
 elif player.lower == "rock" and computer == "scissors" :
  print(computer)
  print("You win!")
 
 elif player.lower == "paper" and computer == "rock" :
  print(computer)
  print("You win!")

 elif player.lower == "scissors" and computer == "paper" :
  print(computer)
  print("You win!")

 else : print("Scissors, Paper, Stone?")
      



        
    
