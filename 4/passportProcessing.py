import csv
    #byr (Birth Year)
    #iyr (Issue Year)
    #eyr (Expiration Year)
    #hgt (Height)
    #hcl (Hair Color)
    #ecl (Eye Color)
    #pid (Passport ID)
    #cid (Country ID)
def getPassportData():
    with open('data.csv','r') as input_file:
        data_str = input_file.read()
        data_array = data_str.split('\n\n')
        passportList = []
        for row in data_array:
            row = row.split()
            passport ={}
            for line in row:
                line = map(str, line.split(':'))
                key, value = line[0], line[1]
                passport[key] = value
            passportList.append(passport)
        #print passportList
        return passportList
def validatePassport(passport):
    valid = 1
    #hgt (Height)
    #hcl (Hair Color)
    #ecl (Eye Color)
    #pid (Passport ID)
    byr = int(passport['byr'])
    if not(byr >= 1920 and byr <= 2002):
        valid = 0
    iyr = int(passport['iyr'])
    if not(iyr >= 2010 and iyr <= 2020):
        valid = 0
    eyr = int(passport['eyr'])
    if not(eyr >= 2020 and eyr <= 2030):
        valid = 0
    hgt = passport['hgt']
    if hgt.endswith('in'):
        valid = 1
    elif hgt.endswith('cm'):
        valid = 1
    else:
        valid = 0
    return valid

def processPassports():
    keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    passportData = getPassportData()
    goodPassports = 0
    for passport in passportData:
        if keys.issubset(passport.keys()):
            goodPassports += 1# validatePassport(passport)
    print goodPassports
    return goodPassports

processPassports()


