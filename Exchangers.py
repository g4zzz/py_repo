# # Задача №1
# # Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
# #     1. На вход обменнику вводишь количество денег int.
# #     2. На выходе в консоль выводится отввет в таком виде:
# #                 "Ты ввёл int (Валюта)"
# #                 "конвертированная сумма в USD = int"
# #     3. Валюту пользователя определите сами.
# while True:
#
#     user_money_1 = input('Type your money amount in RUB (exclude coins) here....')
#
#     if not user_money_1.isdigit():
#         print('You typed incorrect amount. Try again')
#         continue
#
#     int_usr_mon_1 = int(user_money_1)
#     print('You typed ', int_usr_mon_1, ' RUB')
#
#     conv_usr_money_1 = int_usr_mon_1 / 72
#     rnd_money_1 = round(conv_usr_money_1, 2)
#     print('Converting sum in USD = ', rnd_money_1)
#
#     break
#
# # Задача №2
# # Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
# #     1. На вход обменнику вводишь количество денег int.
# #     2. На выходе в консоль выводится ответ в таком виде:
# #                 "Ты ввёл int (Валюта)"
# #                 "Конвертированная сумма в USD = int"
# #                 "Конвертированная сумма в EUR = int"
# #                 "Конвертированная сумма в CHF = int"
# #                 "Конвертированная сумма в GBP = int"
# #                 "Конвертированная сумма в CNY = int"
# #     3. Валюту пользователя определите сами.
#
# while True:
#
#     usr_money_2 = input('Type your money amount in RUB (exclude coins) here....')
#
#     if not usr_money_2.isdigit():
#         print('You typed incorrect amount. Try again')
#         continue
#
#     int_usr_mon_2 = int(usr_money_2)
#     print('You typed ', int_usr_mon_2, ' RUB')
#
#     conv_usr_money_usd_2 = int_usr_mon_2 / 72
#     rnd_money_usd_2 = round(conv_usr_money_usd_2, 2)
#     print('Converting sum in USD = ', rnd_money_usd_2)
#
#     conv_usr_money_eur_2 = int_usr_mon_2 / 86
#     conv_usr_money_eur_2 = round(conv_usr_money_eur_2, 2)
#     print('Converting sum in EUR = ', conv_usr_money_eur_2)
#
#     conv_usr_money_chf_2 = int_usr_mon_2 / 79
#     conv_usr_money_chf_2 = round(conv_usr_money_chf_2, 2)
#     print('Converting sum in CHF = ', conv_usr_money_chf_2)
#
#     conv_usr_money_gbp_2 = int_usr_mon_2 / 101
#     conv_usr_money_gbp_2 = round(conv_usr_money_gbp_2, 2)
#     print('Converting sum in GBP = ', conv_usr_money_gbp_2)
#
#     conv_usr_money_cny_2 = int_usr_mon_2 / 11
#     conv_usr_money_cny_2 = round(conv_usr_money_cny_2, 2)
#     print('Converting sum in CNY = ', conv_usr_money_cny_2)
#
#     break


# Задача №3
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

# while True:
#
#     usr_money_3 = input('Type your money amount in RUB (exclude coins) here....')
#     try:
#         usr_money_3_int = int(usr_money_3)
#
#     except ValueError:
#         if not usr_money_3:
#             print('You inserted empty field. Please insert a number')
#             continue
#         else:
#             print('You inserted not a number. Please insert a number')
#             continue
#     if int(usr_money_3) < 0:
#         print('Please insert positive amount')
#         continue
#
#
#     int_usr_mon_3 = int(usr_money_3)
#     print('You typed ', int_usr_mon_3, ' RUB')
#
#     conv_usr_money_usd_3 = int_usr_mon_3 / 72
#     rnd_money_usd_3 = round(conv_usr_money_usd_3, 2)
#     print('Converting sum in USD = ', rnd_money_usd_3)
#
#     conv_usr_money_eur_3 = int_usr_mon_3 / 86
#     conv_usr_money_eur_3 = round(conv_usr_money_eur_3, 2)
#     print('Converting sum in EUR = ', conv_usr_money_eur_3)
#
#     conv_usr_money_chf_3 = int_usr_mon_3 / 79
#     conv_usr_money_chf_3 = round(conv_usr_money_chf_3, 2)
#     print('Converting sum in CHF = ', conv_usr_money_chf_3)
#
#     conv_usr_money_gbp_3 = int_usr_mon_3 / 101
#     conv_usr_money_gbp_3 = round(conv_usr_money_gbp_3, 2)
#     print('Converting sum in GBP = ', conv_usr_money_gbp_3)
#
#     conv_usr_money_cny_3 = int_usr_mon_3 / 11
#     conv_usr_money_cny_3 = round(conv_usr_money_cny_3, 2)
#     print('Converting sum in CNY = ', conv_usr_money_cny_3)
#     break

# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.