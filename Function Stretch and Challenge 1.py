#Jeeson Baktha
#Stretch and Challenge 1
#4 December 2014


#FUNCTIONS

def first_convert(inch, feet):
    feet = inch / 12
    inch = feet * 12
    print("{0} feet/foot is {1} inch(es)".format(feet, inch))



inch1 = int(input("Please enter the amount of inches: "))
feet1 = int(input("Please enter the amouut of feet: "))

first_convert(inch, feet)
