print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You are on a cross road, do you want to go right into the woods or left over the field?")
direction = input("left or right")
if direction == "left":
    print("You walked through the woods and came to a river, there is no bridge to cross the river. What are you going to do? Swim or wait?")
    choice = input ("wait or swim")
    if choice =="wait":
        print("That was a smart decicion, since the river is full of thouts. A boot came and the fairman brought you safe to the other side.")
        print("You walked a little bit ad came to a house with three doors.")
        print("The doors are blue, red and yellow. Which one do you choose?")
        doors = input("red / blue / yellow / walk away")
        if doors == "red":
            print("You ope the door and flames spike out. I'm sorry put it is Game over for you.")
        elif doors == "blue":
            print("As soon you open the door a lion jumps out and eats you. Game over!")
        elif doors == "walk away":
            print("That was the wrong decision. You lost!")
        else:
            print("You opened the door and see the treasur box. Congratulations you won!")
    else:        
        print("You got attacked by the river monster and died. Game over!")
else:
    print("You didn't saw the hole in the ground and fell into it. You hit your head and died. Game over.")