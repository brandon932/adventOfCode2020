def getData():
    with open('data.csv') as data_file:
        data = data_file.read()
        bagsList = list(filter(None,data.split('\n')))
        print bagsList
        return bagsList
getData()

