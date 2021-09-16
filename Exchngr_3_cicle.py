# Задача №3
#  Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
#             "Ты ввёл int (Валюта)"
#             "конвертированная сумма в USD = int"
#             "конвертированная сумма в EUR = int"
#             "конвертированная сумма в CHF = int"
#             "конвертированная сумма в GBP = int"
#             "конвертированная сумма в CNY = int"
# 3. Скрипт должен выдать сообщение
#             "Введите положительное число." Если число меньше 0.
#             "Вы ввели не число. Введите число." Если введены буквы.
#             "Вы ввели пустое поле. Введите число." Если введено пустое значение.

while True:

    usr_money_3 = input('Type your money amount in RUB (exclude coins) here....')
    try:
        usr_money_3_int = int(usr_money_3)

    except ValueError:
        if not usr_money_3:
            print('You inserted empty field. Please insert a number')
            continue
        else:
            print('You inserted not a number. Please insert a number')
            continue
    if int(usr_money_3) < 0:
        print('Please insert positive amount')

    int_usr_mon_3 = int(usr_money_3)
    print('You typed ', int_usr_mon_3, ' RUB')

    conv_usr_money_usd_3 = int_usr_mon_3 / 72
    rnd_money_usd_3 = round(conv_usr_money_usd_3, 2)
    print('Converting sum in USD = ', rnd_money_usd_3)

    conv_usr_money_eur_3 = int_usr_mon_3 / 86
    conv_usr_money_eur_3 = round(conv_usr_money_eur_3, 2)
    print('Converting sum in EUR = ', conv_usr_money_eur_3)

    conv_usr_money_chf_3 = int_usr_mon_3 / 79
    conv_usr_money_chf_3 = round(conv_usr_money_chf_3, 2)
    print('Converting sum in CHF = ', conv_usr_money_chf_3)

    conv_usr_money_gbp_3 = int_usr_mon_3 / 101
    conv_usr_money_gbp_3 = round(conv_usr_money_gbp_3, 2)
    print('Converting sum in GBP = ', conv_usr_money_gbp_3)

    conv_usr_money_cny_3 = int_usr_mon_3 / 11
    conv_usr_money_cny_3 = round(conv_usr_money_cny_3, 2)
    print('Converting sum in CNY = ', conv_usr_money_cny_3)
    break
