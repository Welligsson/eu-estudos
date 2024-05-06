# Which number do you want to check?
# number = int(input('digite um numero: '))

# if number % 2 == 0:
#   print("o numero é par")
# else:
#   print("o numero é impar")


#### imc
# height = float(input('altura em metros: '))  # in meters e.g., 1.55
# weight = int(input('kg: '))  # in kilograms e.g., 72
# # Your code below this line 👇
# bmi = weight / (height * height)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")

### ano bissexto
# ano = int(input('digite o ano: '))

# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
#     print(f'o ano {ano} é bissexto!')
# else:
#     print(f'o ano {ano} não é bissexto!')

### montanha russa
# print("Welcome to the rollercoaster!")
# altura = int(input("What is your height in cm? "))
# preço = 0

# if altura >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("qual sua altura "))
#   if age < 12:
#     preço = 5
#     print("tickets crianças $5.")
#   elif age <= 18:
#     preço = 7
#     print("tickets joven $7.")
#   else:
#     preço = 12
#     print("tickets adultos $12.")
  
#   foto = input("DEseja tirar foto? Y or N. ")
#   if foto == "Y":
#     preço += 3
  
#   print(f"o preço final do ingresso é ${preço}")

#### True love
# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("t")
# o = lower_names.count("r")
# v = lower_names.count("u")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")


### tesouro
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
choice1 = input("you're at a crossroad, where do you want to go? Type 'left' or 'right'").lower()

if choice1 == 'left':
    choice2 = input('you\'ve come to a lake. There is an island in the middle of the lake.type "wait" to wait for a boat. Type "swim" to swim a cross.').lower()
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print('you got attacked by an angry trout. game over.')
else:
    print('voce caiu em um buraco, Game Over.')

