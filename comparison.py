
# 1) Create two different variables type of String
name_1, name_2 = 'Alexandr', 'Vasiliy'

# 2) Create four different variables type of Int
height_1, height_2, height_3, height_4 = 180, 175, 170, 165

# 3) Create free different variables type of Float
length_1, length_2, length_3 = 15.5, 17.8, 4.2

# 4) Compare variables Int 15 times using operators >, <, >=, <=, !=. Result prints to a console
if height_1 > height_2:
    print('height', name_1, '=', height_1, 'cm')
elif height_1 < height_2:
    print('height', name_2, '=', height_2, 'cm')
elif height_1 >= height_2:
    print('height', name_1, '=', height_1, 'cm')
elif height_1 <= height_2:
    print('height', name_2, '=', height_2, 'cm')
elif height_1 != height_2:
    print('height', name_1, '=', height_1, 'cm')
if height_4 > height_3:
    print('someone`s height', '=', height_4, 'cm')
elif height_4 < height_3:
    print('height_3 =', height_3, 'cm')
elif height_4 >= height_3:
    print('height_4 =', height_4, 'cm')
elif height_4 <= height_3:
    print('height_3 =', height_3, 'cm')
elif height_4 != height_3:
    print('height_4 =', height_4, 'cm')
if height_2 > height_3:
    print('height', name_2, '=', height_2, 'cm')
elif height_2 < height_3:
    print('height_3 =', height_3, 'cm')
elif height_2 >= height_3:
    print('height', name_2, '=', height_2, 'cm')
elif height_2 <= height_3:
    print('height_3 =', height_3, 'cm')
elif height_2 != height_3:
    print('height', name_2, '=', height_2, 'cm')
else:
    print("Nothing happened")

# 5) Compare variables Float 9 times using operators >, <, >=, <=, !=. Result prints to a console
if length_1 > length_2:
    print('length', name_1, '=', length_1, 'inches')
elif length_1 < length_2:
    print('length', name_2, '=', length_2, 'inches')
elif length_1 >= length_2:
    print('length', name_1, '=', length_1, 'inches')
elif length_1 <= length_2:
    print('length_2 =', name_2, length_2, 'inches')
elif length_1 != length_2:
    print('length', name_1, '=', length_1, 'inches')
if length_1 > length_3:
    print('length', name_1, '=', length_1, 'inches')
elif length_1 < length_3:
    print('length_3 =', length_3, 'inches')
elif length_1 >= length_3:
    print('length', name_1, '=', length_1, 'inches')
elif length_1 <= length_3:
    print('length_3 =', length_3, 'inches')
else:
    print("I hope somebody will read this text")

# 6) Compare variables Int 6 times with operators >, <, >=, <=, != , and, or, not. Print to a console.
name_3, name_4 = 'John', 'Dan'
length_4 = 18.2

if height_1 >= height_2 and length_1 > length_2:
    print('You are the best,', name_1)
print(name_1, 'not better than', name_2)

if height_1 > height_2 or length_1 >= length_2:
    print('but somewhat he has')

if not height_4 <= height_3 and length_3 != length_4:
    print('You are the best,', name_3)
print(name_3, 'not better than', name_4, 'too')


# 7) Use script with function input().
#     1. The function must accept an Integer as input.
#     2. Output must "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
print('Please insert a Integer number')
value = input()
if value.isdigit():
    if int(value) == 30:
        print('Вы вели число =', value, 'которое равно 30')
    if int(value) > 30:
        print('Вы вели число =', value, 'которое больше 30')
    if int(value) < 30:
        print('Вы вели число =', value, 'которое меньше 30')
else:
    print('Insert correct number')

# 8) Use script with function input().
#     1. The function must accept an Integer as input.
#     2. A random Integer must be generated inside the function (import random)...(random.randint(1, 100))
#     3. Output must "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"
print('Please insert a Integer number to compare random')
value_rand1 = input()
if value_rand1.isdigit():
    import random
    num_rand = random.randint(1, 100)
    if int(value_rand1) == num_rand:
        print('Вы вели число =', value_rand1, 'которое равно сгенерированному числу', num_rand)
    if int(value_rand1) > num_rand:
        print('Вы вели число =', value_rand1, 'которое больше сгенерированного числа', num_rand)
    if int(value_rand1) < num_rand:
        print('Вы вели число =', value_rand1, 'которое меньше сгенерированного числа', num_rand)
else:
    print('Insert correct number')

# 9) Use script with function input().
#      1. The function must accept an Integer as input.
#      2. Random two Integers must be generated inside the function (import random)...(random.randint(1, 100))
#      3. Output must "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
print('Please insert a Integer number to compare TWO random')
value_rand2 = input()
if value_rand2.isdigit():
    import random
    num_rand1 = random.randint(1, 100)
    num_rand2 = random.randint(1, 100)
    if num_rand1 == int(value_rand2) > num_rand2:
        print('Вы вели число =', value_rand2, 'которое равно 1-му сгенерированному числу', num_rand1, 'и больше 2-го числа', num_rand2)

    if num_rand1 == int(value_rand2) < num_rand2:
        print('Вы вели число =', value_rand2, 'которое равно 1-му сгенерированному числу', num_rand1, 'и меньше 2-го числа', num_rand2)

    if num_rand1 < int(value_rand2) == num_rand2:
        print('Вы вели число =', value_rand2, 'которое больше 1-го сгенерированного числа', num_rand1, 'и равно 2-му числу', num_rand2)

    if num_rand1 > int(value_rand2) == num_rand2:
        print('Вы вели число =', value_rand2, 'которое меньше 1-го сгенерированного числа', num_rand1, 'и равно 2-му числу', num_rand2)

    if num_rand1 > int(value_rand2) > num_rand2:
        print('Вы вели число =', value_rand2, 'которое меньше 1-го сгенерированного числа', num_rand1, 'и больше 2-го числа', num_rand2)

    if num_rand1 > int(value_rand2) < num_rand2:
        print('Вы вели число =', value_rand2, 'которое меньше 1-го сгенерированного числа', num_rand1, 'и меньше 2-го числа', num_rand2)

    if num_rand1 < int(value_rand2) > num_rand2:
        print('Вы вели число =', value_rand2, 'которое больше 1-го сгенерированного числа', num_rand1, 'и больше 2-го числа', num_rand2)

    if num_rand1 < int(value_rand2) < num_rand2:
        print('Вы вели число =', value_rand2, 'которое больше 1-го сгенерированного числа', num_rand1, 'и меньше 2-го числа', num_rand2)
else:
    print('Insert correct number')
