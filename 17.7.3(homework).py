per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите число: "))
deposit=[int(per_cent.get('ТКБ')*money/100),
         int(per_cent.get('СКБ')*money/100),
         int(per_cent.get('ВТБ')*money/100),
         int(per_cent.get('СБЕР')*money/100)]
print('Максимальная сумма, которую вы можете заработать - %d ' %max(deposit))
