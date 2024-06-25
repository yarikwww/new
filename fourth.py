#Вправа 4
import csv


results = []


with open('game_results.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        player_name = row[0].strip()
        score = int(row[1].strip())
        results.append((player_name, score))


highest_scores = {}

for player, score in results:
    if player in highest_scores:

        if score > highest_scores[player]:
            highest_scores[player] = score
    else:

        highest_scores[player] = score


sorted_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)


with open('high_scores.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Ім\'я гравця', 'найвищий бал'])
    csvwriter.writerows(sorted_scores)

print("Результати були збережені у файлі high_scores.csv")