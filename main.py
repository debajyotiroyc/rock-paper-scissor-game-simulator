import random as rd
game=['rock','paper','scissor']
name1=input("Enter the name of player 1: ")
name2=input("Enter the name of player 2: ")
rounds=input("How many rounds do you want to play? ")
rounds=int(rounds)
c1,c2=0,0
for i in range(rounds):
    hand1=rd.choice(game)
    hand2=rd.choice(game)
    print("Player",name1,"has chosen:",hand1)
    print("Player",name2, "has chosen:", hand2)

    if hand1=='scissor' and hand2=='paper':
        c1=c1+1
        print("point goes to player",name1)
    elif hand2=='scissor' and hand1=='paper':
        c2=c2+1
        print("point goes to player", name2)
    if hand1=='paper' and hand2=='rock':
        c1=c1+1
        print("point goes to player", name1)
    elif hand2=='paper' and hand1=='rock':
        c2=c2+1
        print("point goes to player", name2)
    if hand1=='rock' and hand2=='scissor':
        c1+=1
        print("point goes to player", name1)
    elif hand2=='rock' and hand1=='scissor':
        c2+=1
        print("point goes to player", name2)
    elif hand1==hand2:
        print("nobody gets a point!")
if c1>c2:
    print("Congratulations player",name1,"on winning the match!!!!!")
elif c2>c1:
    print("Congratulations player",name2, "on winning the match!!!!!")
else:
    print("The contest ended on equal terms!!!!It's a draw!!")
print("The final scores are: ")
print("Player",name1,":",c1)
print("Player",name2,":",c2)
print("Thank you for playing!!!!")




