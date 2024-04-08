import random 
import time
num1 = random.randint(0,10)
num2 = random.randint(0,10)

# DEFINE ALL THE QUESTIONS AND ANSWERS first.

additionqn = str(num1) + ' + ' + str(num2) + ' =' + ' ?'
additionanswer = num1 + num2

multiplicationqn = str(num1)+ ' * '+ str(num2)+ ' =' + ' ?'
multiplicationans = num1*num2

divisionqn = str(num1) + ' / ' + str(num2) + ' =' + ' ?'
divisionans = int(num1/num2)

minusqn = str(num1) + ' - ' + str(num2) + ' =' + ' ?'
minusans = num1-num2


print('====MATH TIMED QUIZ====')



chosen_operator = input('choose an operator : -, +, *, /')

if chosen_operator == '+' :
    print('Here is your question')
    start_time = time.time()
    print (additionqn)
    
    playeranswer = int(input('Enter your answer'))
    end_time = time.time()
    totaltime = end_time - start_time
    if playeranswer == additionanswer :
         print("Good Job. You got it right!")
         print('You did it in...')
         print (totaltime, 'seconds!' )
    else : print("Wrong answer.. Think again!")

elif  chosen_operator == '*' :
    print(multiplicationqn)
    start_time = time.time()
    playeranswer = int(input('Enter your answer'))
    end_time = time.time()
    totaltime = end_time - start_time
    if playeranswer == multiplicationans :
     print('You got it right! In..', totaltime, 'seconds!')
    else : print("Wrong answer.. Think again!")
          
elif chosen_operator == '/'  :
      print('If answer is a decimal, then Answer to the according integer.')
      print(divisionqn)
      start_time = time.time()
      playeranswer = int(input('Enter your answer'))
      end_time = time.time()
      totaltime = end_time - start_time
      if playeranswer == divisionans :
          print('You got it right! In..', totaltime, 'seconds!')
      else : print("Wrong answer.. Think again!")
      
elif chosen_operator == '-'  :
      print(minusqn)
      start_time = time.time()
      playeranswer = int(input('Enter your answer'))
      end_time = time.time()
      totaltime = end_time - start_time
      if playeranswer == minusans :
          print('You got it right! In..', totaltime, 'seconds!')
      else : print("Wrong answer.. Think again!")
    
