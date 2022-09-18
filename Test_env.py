per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Сумма вклада:")
deposit_per_cent = list(per_cent.values())
deposit = [num * int(money)/100 for num in deposit_per_cent]
deposit = [int(x) for x in deposit]
max_deposit = max(deposit)
print("Накопленные средства на вкладе за год в разных банках:", deposit)
print("Максимальная сумма, которую вы можете заработать —", max_deposit)