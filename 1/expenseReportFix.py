import csv
value = input("please enter 1 for first and 2 for seccond challenge: ")
def get_expenses():
    with open('expenseReport.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\b")
        expenses = []
        for row in csv_reader:
            expenses.append(row[0])
        return expenses
def my_func():
    expenses = get_expenses()
    for expense in expenses:
        x = int(expense)
        dif = 2020 - x
        if str(dif) in expenses:
            num = dif * x
            print str(x)+ "*" + str(dif) + "=" + str(num)
            return num

def seccond():
    #enter second part of puzzle here/ find 3 numbers that sum to 2020
    #and return the product
    expenses = get_expenses()
    for x in expenses:
        for y in expenses:
            z = 2020 - int(x) - int(y)
            if str(z) in expenses:
                num = int(x)*int(y)*z
                print num
                return num


                


    print("hello world")

if value == 1:
    my_func()
elif value == 2:
    seccond()

