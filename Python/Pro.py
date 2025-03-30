import random # this is a function which will help you choose random number

while True: #this keeps the program run with out stoping

 choice = input("roll the dice(y/n): ")#this this the program which let you playing the game
 if choice == 'y':
  A = random.randint(1,6)
  B = random.randint(1,6)
  print(f'({A},{B})')
 elif choice == 'n':#and this is the on which you can press if you want to stop playing
  print("thank for playin")#and this is the one which let you know if you have entered an wrong thing 
  break
 else:
  print('invalide only enter  y/n')