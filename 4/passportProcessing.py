import csv
import re
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
        hgt = int(hgt[0:-2])
        if not(hgt>= 59 and hgt <= 76):
            valid = 0

    elif hgt.endswith('cm'):
        hgt = int(hgt[0:-2])
        if not(hgt >= 150 and hgt <= 193):
            valid = 0
    else:
        valid = 0

    hcl = passport['hcl']
    match = re.findall("(#[A-Fa-f0-9]{6})", hcl)
    if not(len(match)) > 0 :
        valid = 0

    eyeColor = {'amb','blu','brn','gry','grn','hzl','oth'}
    ecl = {passport['ecl']}
    if not(ecl.issubset(eyeColor)):
       valid = 0

    pid = passport['pid']
    validId = len(pid) == 9
    if not(validId):
        valid = 0
    return valid

def processPassports():
    keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    passportData = getPassportData()
    goodPassports = 0
    for passport in passportData:
        if keys.issubset(passport.keys()):
            goodPassports += validatePassport(passport)
    print goodPassports
    return goodPassports

processPassports()


