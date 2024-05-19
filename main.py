import random
randomGenerated_outcome = random.randrange(1, 4)

if randomGenerated_outcome == 1:
    computer = "s"
elif randomGenerated_outcome == 2:
    computer = "p"
elif randomGenerated_outcome == 3:
    computer = "x"
else:
    pass

print("\n")
print("      <Game Started>      ")
print("\n")
user_input = input("Your Turn:\nStone(s) Paper(p) or scissores(x): ")
print("Computer Turn:\nStone(s) Paper(p) or scissores(x):", computer)

def game(computer, user):
    if computer == user:
        return "draw"
    elif computer == "s":
        if user == "p":
            return True
        elif user == "x":
            return False
    elif computer == "p":
        if user == "x":
            return True
        elif user == "s":
            return False
    elif computer == "x":
        if user == "s":
            return True
        elif user == "p":
            return False
    else:
        pass


output = game(computer, user_input)
if output == "draw":
    print("   ***   Matdh Draw   ***   ")
elif output == True:
    print("   ***   You Won   ***   ")
elif output == False:
    print("   ***   You Lose   ***   ")
else:
    print("   ***   Choose One Of The Options   ***   ")

print("\n")
print("      </Game Over>      ")
print("\n") 