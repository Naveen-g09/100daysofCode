import random

print("Welcome to Rock, Paper Scissor")
a = int(input("Enter 0 for rock, 1 for Scissors, 2 for paper: "))
comp = random.randint(0, 2)
if a==comp:
    print("match draw")
elif a==0 and comp==1:
    print("You chose rock, computer chose scissors \n you won!")
elif a==0 and comp==2:
    print("You chose rock, computer chose paper \n you lose!")
elif a==1 and comp==0:
    print("You chose scissors and computer chose rock \n so you lose")
elif a==1 and comp==2:
    print("You chose scissors, computer chose paper \n you Won!")
elif a==2 and comp==0:
    print("You chose paper, computer chose rock \n you won!")
elif a==2 and comp==1:
    print("You chose paper, computer chose scissors \n you lose!")
else:
    print(f"wrong input maybe you gave: {a}")