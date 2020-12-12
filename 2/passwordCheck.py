import csv
def parse_csv():
    data = []
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter= " ")
        for row in csv_reader:
            dataRow = []
            x = row[0].split('-')
            dataRow.append(x)
            dataRow.append(row[1][0])
            dataRow.append(row[2])
            data.append(dataRow)
        return data

def check_passwords_sled():
    correctPasswords = 0
    passwordList = parse_csv()
    for row in passwordList:
        num = row[2].count(row[1])
        if  num >= int(row[0][0]) and num <= int(row[0][1]):
            correctPasswords += 1
    print correctPasswords
    return correctPasswords

def check_passwords_toboggan():
    correctPasswords = 0
    passwordList = parse_csv()
    for row in passwordList:
        x = int(row[0][0])-1
        y = int(row[0][1])-1
        #print row
        #print row[2][x]
        if row[2][x] == row[1] or row[2][y] == row[1]:
            if not(row[2][x] == row[1] and row[2][y] == row[1]):
                correctPasswords += 1
    print correctPasswords
    return correctPasswords


check_passwords_toboggan()

