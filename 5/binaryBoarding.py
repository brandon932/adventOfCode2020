def scanData():
    with open("data.csv") as input_file:
        data_str = input_file.read()
        bordingPassArray = data_str.split('\n')
        return bordingPassArray

def convertToInt(binaryString):
    string = binaryString.replace("F","0")
    string = string.replace("B","1")
    string = string.replace("L","0")
    string = string.replace("R","1")
    return int(string, 2)

def getBordingPassId():
    higestPassId = 0
    passList = scanData()
    for data in passList:
        row = convertToInt(data[:7])
        seat = convertToInt(data[-3:])
        passId = (row * 8) + seat
        if passId> higestPassId:
            higestPassId = passId
        print higestPassId
    return higestPassId

getBordingPassId()


