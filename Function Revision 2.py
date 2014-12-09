#Jeeson Baktha
#Function Revision 2
#25 November 2014


#FUNCTIONS

def triangle():
    star_width= int(input("Please enter an odd number of stars to display in a triangle"))

    for count in range(star_width, 0, -2):
        
        print(("*" * count).center(star_width))

#MAIN PROGRAM
        
triangle()


