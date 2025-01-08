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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'? ").lower()
if 'left' in choice_1:
    choice_2 = input("You've come to a lake. "
                      "There is an island in the middle of the lake. "
                      "Type 'wait' to wait fora a boat. "
                      "Type 'swim' to swim across.").lower()
    if 'wait' in choice_2:
        choice_3 = input("You arrive at the island unharmed"
                         "There is house with 3 doors: "
                         "One red, one blue, one yellow."
                         "Which colour do you choose?").lower()
        if 'red' in choice_3:
            print("Burned by fire.")
            print("Game Over.")
        elif 'rlue' in choice_3:
            print("Eaten by beasts.")
            print("Game Over.")
        elif 'yellow' in choice_3:
            print('You Win!')
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.")
        print("Game Over.")
else:
    print("Fall into a hole.")
    print("Game Over.")

