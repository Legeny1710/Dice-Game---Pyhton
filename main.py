import time
import random

print("Welcome to Dice game...")
time.sleep(0.4)
print("Let's start by checking your usernames!")
time.sleep(0.6)

#Username Check
user1 = input("What is your user name?(User1):")
time.sleep(0.4)
user2 = input("What is your user name?(User2):")
time.sleep(0.4)

def vnmatch(a):
  vn = open("validnames.txt", "r")
  readfile = vn.read()  
  while a not in readfile:
    time.sleep(0.4) 
    print('Your username is not valid!',a ,', You cannot Play!!!')
    a = input("What is your user name?")
  else:
   print("You can Play!!!", a)
    
  vn.close() 
  
vnmatch(user1)
vnmatch(user2)


print("Let's start then!")


player1 = 0
player2 = 0

#Actual Game
def roll_dice(a,b):
  for i in range(5):
    print('Round {}'.format(i))
    valueOne = random.randint(1,6)
    valueOne2 = random.randint(1,6)
    print("Player 1's turn")
    if valueOne == valueOne2:
      print("You got double!")
      a += 5
    else:
      print("Player 1 rolled ", valueOne, "The other one...", valueOne2)
      if valueOne % 2 == 0: 
        print("First dice...")
        print("It is even, you get 10 points")
        a = a + 10
      else:
        print("First dice...")
        print("It is odd, you get -5 points ")
        a = a - 5

      if valueOne2 % 2 == 0: 
        print("Second dice...")
        print("It is even, you get 10 points")
        a = a + 10
      else:
        print("Second dice...")
        print("It is odd, you get -5 points ")
        a = a - 5

      if valueOne == valueOne2:
        print("You got double!, Here is your another chance")
        print("dice rolled...", valueOne)





#SECOND PLAYER
    time.sleep(0.5)
    print(" Player 2 it's your turn")

    valueTwo = random.randint(1,6)
    valueTwo2 = random.randint(1,6)
    if valueTwo == valueTwo2:
      print("You got double!, Here is your another chance")
      print("dice rolled...", valueTwo)
      time.sleep(0.5)
      print("Player 2 rolled ",  valueTwo)
      if valueTwo % 2 == 0:
        print("It is even, you get 10 points")
        b = b + 10
      else:
        print("First dice...")
        print("It is odd, you get -5 points")
        b = b - 5
      time.sleep(0.5)

    else:
      print("Player 2 rolled ",  valueTwo)
      if valueTwo % 2 == 0:
        print("It is even, you get 10 points")
        b = b + 10
      else:
        print("First dice...")
        print("It is odd, you get -5 points")
        b = b - 5
      time.sleep(0.5)

      if valueTwo2 % 2 == 0: 
        print("Second dice...", valueTwo2)
        print("It is even, you get 10 points")
        b = b + 10
      else:
        print("Second dice...", valueTwo)
        print("It is odd, you get -5 points")
        b = b - 5

      if valueTwo == valueTwo2:
        print("You got double!, Here is your another chance")
        print("dice rolled...", valueTwo)
      time.sleep(0.5)
    
    print("...")
    print("...")
    print("...")

  if a < 0 :
    a = 0
  else:
    a = a

  if b < 0 :
    b = 0
  else:
    b = b

  print("Here is the results: PLayer 1 ==", a, " Player 2 ==", b)

  if a < b:
    print("Winner is.....")
    time.sleep(1)
    print("PLAYER 2")
    file = open("winners.txt", "a")
    file.write(" User name: " + user2 + "|" + " Score: " + str(b) + "|" + "\n\n")
    file.close()
  elif a > b:
    print("Winner is.....")
    time.sleep(1)
    print("PLAYER 1")
    file = open("winners.txt", "a")
    file.write(" User name: " + user1 + "|" + " Score: " + str(a) + "|" + "\n\n")
    file.close()
  else:
    time.sleep(1)
    valueOne = random.randint(1, 6)
    valueOne2 = random.randint(1, 6)
    print("DRAW!!!")
    print("One more dice to deicide who is champion!")
    print("player1... dice rolled...", valueOne)
    print("player2... dice rolled...", valueOne2)
    if valueOne < valueOne2:
      print("The winner is Player2")
      file = open("winners.txt", "a")
      file.write(" User name: " + user2 + "|" + " Score: " + str(b) + "|" + "\n\n")
      file.close()
    elif valueOne > valueOne2:
      print("The winner is Player1")
      file = open("winners.txt", "a")
      file.write(" User name: " + user1 + "|" + " Score: " + str(a) + "|" + "\n\n")
      file.close()


roll_dice(player1,player2)  
