import random

# #### random inteiro
# random_inteiro = random.randint(1 , 10)
# print(random_inteiro)


# ### random float
# random_float = random.random() * random.randint(0, 5)
# print(random_float)


## cara ou coroa
# import random

# random_side = random.randint(0, 1)
# if random_side == 1:
#   print("cara")
# else:
#   print("coroa")

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# letter = position[0].lower()
# abc = ['a', 'b', 'c']
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = 'X'

# print(f"{line1}\n{line2}\n{line3}")

### pedra papel tesoura
import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
b = random.randint(1,3)
print (b)
if a == b:
    print ("EMPATE")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")