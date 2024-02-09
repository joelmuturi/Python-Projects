#project treasure land
print("Welcome to treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("is it left or right? 'left' or 'right': ")
if choice1 == 'left':
    choice2 = input("is it swim or wait? 'swim' or 'wait': ")
    if choice2 == 'wait':
        choice3 = input("which color? 'red', 'blue' or 'yellow': ")
        if choice3 == 'red':
            print("game over")
        elif choice3 == 'blue':
            print("game over")
        elif choice3 == 'yellow':
            print("you win")
        else:
            print("the colour doesn't exist")
    else:
        print("game over")
else:
    print("game over")

