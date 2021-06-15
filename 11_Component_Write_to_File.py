import csv


def get_score(y):
    return y[1]


loop = ""
while loop == "":
    name_input = input("enter a name: ")
    score_input = input("enter a score: ")
    csv_file = open("test_leaderboard.csv", "r")
    leaderboard_list = []
    written = 0
    for x in csv.reader(csv_file):
        leaderboard_list.append(x)
    entry = [name_input, score_input]
    leaderboard_list.append(entry)
    csv_file.close()
    csv_file = open("test_leaderboard.csv", "a", newline='')
    leaderboard_list.sort(key=get_score, reverse=True)
    writer = csv.writer(csv_file)
    for x in leaderboard_list:
        writer.writerow(x)
    for x in leaderboard_list:
        print(x)

    csv_file.close()