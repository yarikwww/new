#Вправа 3
import random
import csv
players = ["Джош", "Лука", "Кейт", "Марка", "Марія"]
results = []
for player in players:
    for _ in range(1):
        score = random.randint(0, 1000)
        results.append((player, score))
with open('game_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Ім\'я гравця', 'рахунок'])
    csvwriter.writerows(results)
print("Результати гри були збережені у файлі game_results.csv")