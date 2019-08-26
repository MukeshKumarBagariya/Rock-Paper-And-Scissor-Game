import random

userscore = 0
comscore = 0
while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
    ch = int(input("User turn: "))
    while ch > 3 or ch < 1:
        ch = int(input("enter valid input: "))
    if ch == 1:
        cname = 'Rock'
    elif ch == 2:
        cname = 'paper'
    else:
        cname = 'scissor'
    print("user choice is: " + cname)
    print("\nNow its computer turn.......")
    cochoice = random.randint(1, 3)
    while cochoice == ch:
        cochoice = random.randint(1, 3)
    if cochoice == 1:
        cochoicename = 'Rock'
    elif cochoice == 2:
        cochoicename = 'paper'
    else:
        cochoicename = 'scissor'
    print("Computer choice is: " + cochoicename)
    print(cname + " V/s " + cochoicename)
    if ((ch == 1 and cochoice == 2) or
            (ch == 2 and cochoice == 1)):
        print("paper wins   ", end="")
        result = "paper"

    elif ((ch == 1 and cochoice == 3) or
          (ch == 3 and cochoice == 1)):
        print("Rock wins =>", end="")
        result = "Rock"
    else:
        print("scissor wins =>", end="")
        result = "scissor"
    if result == cname:
        print("  User wins  ")
        userscore=userscore+1
        print('And you score is {}'.format(userscore))
    else:
        print("  Computer wins  ")
        comscore=comscore+1
        print('computer score is {}'.format(comscore))


    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")
