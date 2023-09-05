import random
program_choice=random.randint(1,3)
user_choice=int(input("Enter your choice 1 for snake 2 for water and 3 for gun"))
upoints=0
ppoints=0
if program_choice==user_choice:
  print("same")
elif program_choice==1 and user_choice==2:
  print("program wins! better luck next time")
  ppoints=ppoints+1
elif program_choice==1 and user_choice==3:
  print("You win!")
  upoints=upoints+1
elif program_choice==2 and user_choice==1:
  print("you win!")
  upoints=upoints+1
elif program_choice==2 and user_choice==3:
  print("program wins! better luck next time")
  ppoints=ppoints+1
elif program_choice==3 and user_choice==1:
  print("program wins! better luck next time")
  ppoints=ppoints+1
elif program_choice==3 and user_choice==2:
  print("You win!")
  upoints=upoints+1
print(program_choice)
print(upoints)
print(ppoints)