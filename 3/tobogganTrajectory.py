import csv
def getData():
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            dataRow = list(row[0])
            data.append(dataRow)
        return data
def findTrees():
    lineCount = 0
    length = 31
    treeCount = 0
    yCount = 0
    data = getData()
    for row in data:
        lineCount += 1
        if row[yCount] == "#":
            treeCount += 1
        yCount += 3
        if yCount >= 30:
            yCount -= length
            #print "resetline :" + str(count) + " y :" + str(yCount) + " tree Count :"+ str(treeCount)
    print treeCount
    return treeCount
findTrees()
