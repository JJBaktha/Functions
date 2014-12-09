#Jeeson Baktha
#Function Development 1
#23/11/14


#FUNCTIONS

def hoursec():
    hours = int(input("Please enter the number of hours: "))
    seconds_1 = (60 * hours) * 60
    return seconds_1

def minsec():
    mins = int(input("Please enter the numbe of minutes: "))
    seconds_2 = mins * 60
    return seconds_2

def secsec():
    seconds_3 = int(input("Please enter the number of seconds: "))
    return seconds_3

def totalsec(hoursec, minsec, secsec):
    total = hoursec() + minsec() + secsec()
    print("This is the total number of seconds: {0}".format(total))


#MAIN PROGRAMS


totalsec(hoursec, minsec, secsec)
