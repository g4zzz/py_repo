# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится ответ в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

while True:

    usr_money_2 = input('Type your money amount in RUB (exclude coins) here....')

    if not usr_money_2.isdigit():
        print('You typed incorrect amount. Try again')

    int_usr_mon_2 = int(usr_money_2)
    print('You typed ', int_usr_mon_2, ' RUB')

    conv_usr_money_usd_2 = int_usr_mon_2 / 72
    rnd_money_usd_2 = round(conv_usr_money_usd_2, 2)
    print('Converting sum in USD = ', rnd_money_usd_2)

    conv_usr_money_eur_2 = int_usr_mon_2 / 86
    conv_usr_money_eur_2 = round(conv_usr_money_eur_2, 2)
    print('Converting sum in EUR = ', conv_usr_money_eur_2)

    conv_usr_money_chf_2 = int_usr_mon_2 / 79
    conv_usr_money_chf_2 = round(conv_usr_money_chf_2, 2)
    print('Converting sum in CHF = ', conv_usr_money_chf_2)

    conv_usr_money_gbp_2 = int_usr_mon_2 / 101
    conv_usr_money_gbp_2 = round(conv_usr_money_gbp_2, 2)
    print('Converting sum in GBP = ', conv_usr_money_gbp_2)

    conv_usr_money_cny_2 = int_usr_mon_2 / 11
    conv_usr_money_cny_2 = round(conv_usr_money_cny_2, 2)
    print('Converting sum in CNY = ', conv_usr_money_cny_2)

    break
