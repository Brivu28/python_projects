import random


comp = random.choice([1,2,3])


youChoice = input("Enter Your Choice")

dict = {
    "stone": 1,
    "paper": 2,
    "scissor":3
    }

revDict = {

     1:"stone",
     2:"paper",
     3:"scissor"
}

youNum = dict[youChoice]

compChoice = revDict[comp]

you = revDict[youNum]

print(f"Your Choice Is {you}\nThe Computer Choice is {compChoice}")


if(compChoice==you):
    print("The Match Is Drawn")

elif(compChoice=="stone" and you=="scissor"):
    print("Computer Won")

elif(compChoice=="stone" and you=="paper"):
    print("Congrats You Won")

elif(compChoice=="scissor" and you=="paper"):
    print("Computer Won")

elif(compChoice=="scissor" and you=="stone"):
    print("Congrats You Won")

elif(compChoice=="paper" and you=="scissor"):
    print("Congrats You Won")

elif(compChoice=="paper" and you=="stone"):
    print("Computer Won")


print("The Game Ended Thank You")


