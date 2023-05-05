import random
life=5
min=0
max=100
guess=0
num=random.randint(0,100)
while life>0:
    print("You can try {} times".format(life))
    guess=int(input("enter a number between {} and {}:".format(min,max)))
    if guess!=num:
        life-=1
    else:
        print("congratulations! it was="+str(num))
        break
    if guess>num:
        max=guess
    elif guess<num:
        min=guess
    if life==0:
        print("You failed:( it was {}".format(guess))