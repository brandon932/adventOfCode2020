def getData():
    with open('data.csv') as data_file:
        data = data_file.read()
        bagsList = list(filter(None,data.split('\n')))
        return bagsList

def getBags(bagDescription):
    data = getData()
    bagList = [bagDescription]
    count = 0
    for bag in bagList:
        for item in data:
            bagData = item.split(" contain")
            bagInList = bagData[1].find(bag) != -1
            dataString = ' '.join(bagList).find( bagData[0])
            if bagInList & dataString:
                bagList.append(bagData[0])
                count += 1

    print count
    print len(bagList)
    return count



getBags('shiny gold bag')
