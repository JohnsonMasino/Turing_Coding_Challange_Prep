from numpy import random

def get_num():
    num = random.randint(1,7)
    return num
   

while True:
    choice = input("Roll The Dice\n Use (y/n): ")    
    if choice == ("y" or "Y"):
        num = get_num()
        print(num)
        print()
        if num == 6:
            print("Roll Again: ")
            num2 = get_num()
            print(num2)
            print()

            if num2 == 6:
                print("You can only get 2 '6's")
                print()

    else:
        print("Concluded !")
        break