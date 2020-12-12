import csv
def getData():
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            dataRow = list(row[0])
            data.append(dataRow)
        return data
def findTrees(x,y):
    lineCount = 0
    length = 31
    treeCount = 0
    yCount = 0
    data = getData()
    for row in data:
        lineCount += 1
        if row[yCount] == "#":
            #something wrong here I think. value too high
            if lineCount % x == 0:
                treeCount += 1
        if lineCount % x == 0:
            yCount += y
        if yCount >= 30:
            yCount -= length
            #print "resetline :" + str(count) + " y :" + str(yCount) + " tree Count :"+ str(treeCount)
    print treeCount
    return treeCount

def calculate_paths():
    paths = [[1,1],[1,3],[1,5],[1,7],[2,1]]
    pathProduct = 1
    for path in paths:
        pathProduct *= findTrees(path[0],path[1])
    print pathProduct
    return pathProduct

calculate_paths()
