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
def kod():
    while True:

        currency = input('Choose your number of currency: USD = 0, EUR = 1, CHF = 2, GBP = 3, CNY = 4 ......')

        cash = input('Type your money amount exclude coins here....')

        try:
            currency = int(currency)
            cash = int(cash)

        except ValueError:
            if not cash or currency:
                print('You inserted empty field. Please insert a number')
                continue
            else:
                print('You inserted not a number. Please insert a number')
                continue
        if int(cash) < 0 or currency < 0:
            print('Please insert positive amount')

        if currency == 0:
            cash_usd = cash / 0.014
            rnd_cash_usd = round(cash_usd, 2)
            message_2 = print('You inserted sum ', cash, ' and currency USD', )
            message_3 = print('converting sum is ', rnd_cash_usd, 'in RUB')
            print(type(rnd_cash_usd))
        if currency == 1:
            cash_eur = cash / 0.012
            rnd_cash_eur = round(cash_eur, 2)
            message_2 = print('You inserted sum ', cash, ' and currency EUR')
            message_3 = print('converting sum is ', rnd_cash_eur, 'in RUB')
        if currency == 2:
            cash_chf = cash / 0.013
            rnd_cash_chf = round(cash_chf, 2)
            message_2 = print('You inserted sum ', cash, ' and currency CHF')
            message_3 = print('converting sum is ', rnd_cash_chf, 'in RUB')
        if currency == 3:
            cash_gbp = cash / 0.01
            rnd_cash_gbp = round(cash_gbp, 2)
            message_2 = print('You inserted sum ', cash, ' and currency GDP')
            message_3 = print('converting sum is ', rnd_cash_gbp, 'in RUB')
        if currency == 4:
            cash_cny = cash / 0.089
            rnd_cash_cny = round(cash_cny, 2)
            message_2 = print('You inserted sum ', cash, ' and currency CNY')
            message_3 = print('converting sum is ', rnd_cash_cny, 'in RUB')

        continue
kod()