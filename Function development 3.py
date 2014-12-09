#Jeeson Baktha
#Function Development 3
#December 2 2014


#ALL FUNCTIONS

def Euro_pound():
    euro = float(input("Please enter the amount of euros: "))
    pound = euro * 0.814
    print("{0} euro(s) is {1:.2f} pound(s)".format(euro, pound))

def Pound_euro():
    pound = float(input("Please enter the amount of pounds: "))
    euro = pound * 1.229
    print("{0} pound(s) is {1:.2f} euro(s)".format(pound, euro))

def Pound_dollar():
    pound = float(input("Please enter the amount of pounds: "))
    dollar = pound * 1.601
    print("{0} pound(s) is {1:.2f} dollar(s)".format(pound, dollar))

def Dollar_pound():
    dollar = float(input("Please enter the amount of dollars: "))
    pound = dollar * 0.625
    print("{0} dollar(s) is {1:.2f} pound(s)".format(dollar, pound))

def Euro_dollar():
    euro = float(input("Please enter the amount of euros: "))
    dollar = euro * 1.302
    print("{0} euro(s) is {1:.2f} dollar(s)".format(euro, dollar))

def Dollar_euro():
    dollar = float(input("Please enter the amount of dollars: "))
    euro = dollar * 0.768
    print("{0} dollar(s) is {1:.2f} euro(s)".format(dollar, euro))

def Pound_chicken():
    pound = float(input("Please enter the amount of pounds: "))
    chicken = pound * 0.2
    print("{0} pound(s) is {1:.2f} chicken(s)".format(pound, chicken))

def Chicken_pound():
    chicken = float(input("Please ente rthe amount of chickens: "))
    pound = chicken * 0.2
    print("{0} chicken(s) is {1:.2f} pound(s)".format(chicken, pound))

def Euro_chicken():
    euro = float(input("Please enter the amount of pounds: "))
    chicken = euro * 0.15
    print("{0} euro(s) is {1:.2f} chicken(s)".format(euro, chicken))

def Chicken_euro():
    chicken = float(input("Please ente rthe amount of chickens: "))
    euro = chicken * 0.16
    print("{0} chicken(s) is {1:.2f} euro(s)".format(chicken, euro))

def Dollar_chicken():
    dollar = float(input("Please enter the amount of pounds: "))
    chicken = dollar * 0.37
    print("{0} dollar(s) is {1:.2f} chicken(s)".format(dollar, chicken))

def Chicken_dollar():
    chicken = float(input("Please enter the amount of chickens: "))
    dollar = chicken * 0.36
    print("{0} chicken(s) is {1:.2f} dollar(s)".format(chicken, dollar))




#MAIN PROGRAM

print("This program will convert between the Euro, US dollar, Chickens and the British Pound.")
print()
print("1 = Euro to Pound\n2 = Pound to Euro\n3 = Pound to Dollar\n4 = Dollar to Pound\n5 = Euro to Dollar\n6 = Dollar to Euro\n7 = Pound to Chicken\n8 = Chicken to pound\n9 = Euro to Chicken\n10 = Chicken to Euro\n11 = Dollar to Chicken\n12 = Chicken to Dollar ")
print()
user_input = 0
while user_input < 1 or user_input > 12:
    user_input = int(input("Please enter the number corrsesponding to the conversion you want to make: "))
if user_input == 1:
    Euro_pound()
elif user_input == 2:
    Pound_euro()
elif user_input == 3:
    Pound_dollar()
elif user_input == 4:
    Dollar_pound()
elif user_input == 5:
    Euro_dollar()
elif user_input == 6:
    Dollar_euro()
elif user_input == 7:
    Pound_chicken()
elif user_input == 8:
    Chicken_pound()
elif user_input == 9:
    Euro_chicken()
elif user_input == 10:
    Chicken_euro()
elif user_input == 11:
    Dollar_chicken()
elif user_input == 12:
    Chicken_dollar() 
else:
    print("What you have entered is not recognisable. Please try again")
    
    
    
