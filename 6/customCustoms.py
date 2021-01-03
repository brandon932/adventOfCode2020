def getData():
    with open("data.csv") as data_file:
        data_str = data_file.read();
        dataArray = data_str.split('\n\n')
        customsArray = [filter(None,data.split('\n')) for data in dataArray]
        return customsArray
def getCustomsLength(customsSheet):
    customSet = set()
    for sheet in customsSheet:
        customSet.update(set(sheet))
    return len(customSet)


def getTotalCustoms():
    count = 0
    customsArray = getData()
    for customsSheet in customsArray:
        count += getCustomsLength(customsSheet)
    print count
    return count
getTotalCustoms()

def checkAllSheets():
    customsArray = getData()
    for customsSheet in customsArray:


