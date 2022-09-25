N = int(input("Количество билетов, приобретаемых на онлайн конференцию: "))
Ages = list()
for i in range(0, N):
    print(f"Возраст поситетеля {i+1}:")
    Ages.insert(i, input())
Ages = [int(x) for x in Ages]
print("Список возрастов участников конференции: ", Ages)
ticket_prices = list()
for i in range(0, N):
    if Ages[i] < 18:
        ticket_prices.insert(i, 0)
    elif 18 <= Ages[i] <= 25:
        ticket_prices.insert(i, 990)
    elif Ages[i] > 25:
        ticket_prices.insert(i, 1390)
print("Список цен на билеты, для каждого участника", ticket_prices)
if N > 3:
    Summ_discount = (9/10)*sum(ticket_prices)
    print("Сумма к оплате с учетом скидки", Summ_discount)
else:
    print("Сумма к оплате за всех участников", sum(ticket_prices))
