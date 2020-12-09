import csv

with open('expenseReport.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\b")
    expenses = []
    for row in csv_reader:
        expenses.append(row[0])
    for expense in expenses:
        x = int(expense)
        dif = 2020 - x
        if str(dif) in expenses:
            num = dif * x
            print str(x)+ "*" + str(dif) + "=" + str(num)


