### média de altura
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f'total heights = {total_height}')

# number_students = 0
# for student in student_heights:
#     number_students += 1
# print(f'number of students = {number_students}')

# average_height = round(total_height / number_students)
# print(f"average height = {average_height}")

### maior pontuação
# student_scores = input().split()
# for number in student_scores:
#     sorted_numbers = sorted(student_scores)
# print(f"The highest score in the class is: {sorted_numbers[-1]}")

### maior pontuação outra resolução
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

# print(f"The highest score in the class is: {highest_score}")

#### numero de gauss
# total = 0
# for n in range(1, 101):
#     total += n
# print(total)

## soma de pares
# target = int(input())
# even_sum = 0
# for number in range(2, target + 1, 2):
#     even_sum += number
# print(even_sum)


### jogo fizzbuzz
# target = int(input())
# for n in range(1, target + 1):
#     if (n % 3 == 0) and (n % 5 == 0):
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)
    


### gerador de senhas
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

### senhas ordenadas
# password = ''
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

## senhas aleatorias
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")