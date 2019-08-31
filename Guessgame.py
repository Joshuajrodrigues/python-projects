import random,sys
count = 1
flag =0
print("GUESS THE NUMBER".center(50))

rand = random.randint(0,9)
print('I have chosen a number between 0 to 9 \nYou\'re\' job is to guess what number I have choosen.'.center(100))
print('You have 5 chances'.center(50))

while count !=6 :
      print("Guess"+ str(count))
      guess = int(input())
      count = count +1
      

      if guess < rand:
          print("Think higher !")


      elif guess > rand:
          print("Think lower !")

      else:
          print("yees! The number is " + str(guess))
          flag = 1
          break
if flag ==1:
    print("thnks for playing, you win".center(50))

else:
    print('sadly you are out of turns'.center(50))
    print('the number was'+ str(rand).center(50))

          
