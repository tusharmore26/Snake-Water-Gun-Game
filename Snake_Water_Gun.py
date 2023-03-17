import random

i=1
ch=0
dr=0
rd=0
while(i<=10):
    rd+=1
    com=random.randint(0, 2)
    print("Round",rd,":")
    user=int(input("Enter 0 for Snake, 1 for Water, 2 for Gun:"))
    if(com==user):
        print("\tMatch Draw")
        dr+=1
    elif(com==0 and user==1):
        print("\tYou Lose")
    elif(com==0 and user==2):
        print("\tYou Won")
        ch+=1
    elif(com==1 and user==0):
        print("\tYou Won")
        ch+=1
    elif(com==1 and user==2):
        print("\tYou Lose")
    elif(com==2 and user==0):
        print("\tYou Lose")
    elif(com==2 and user==1):
        print("\tYou Won")
        ch+=1
    else:
        print("\tPlease enter correct value!!")
    i+=1

if(ch==0):
    print("You lose all rounds, Better Luck next Time!!")
else:
    print("\t\tCongrats You won",ch," rounds!!")
    print("\t\t And",dr,"rounds are draw!!")


