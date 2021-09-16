# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.
while True:

    user_money_1 = input('Type your money amount in RUB (exclude coins) here....')

    if not user_money_1.isdigit():
        print('You typed incorrect amount. Try again')

    int_usr_mon_1 = int(user_money_1)
    print('You typed ', int_usr_mon_1, ' RUB')

    conv_usr_money_1 = int_usr_mon_1 / 72
    rnd_money_1 = round(conv_usr_money_1, 2)
    print('Converting sum in USD = ', rnd_money_1)

    break
