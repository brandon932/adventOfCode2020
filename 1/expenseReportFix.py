import csv
value = input("please enter 1 for first and 2 for seccond challenge: ")
def my_func():
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
                return num

def seccond():
    print("hello world")

if value == 1:
    my_func()
elif value == 2:
    seccond()

