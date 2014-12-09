#Jeeson Baktha
#function Development 2
#1 December 2014


#FUNCTIONS


def upTriangle():
    
    for count in range(1, star_width + 1, 2):
        print(("*" * count).center(star_width,'+'))

        
        
def downTriangle():

    for count in range(star_width - 2, 0, -2):
        print(("*" * count).center(star_width,'+'))



#MAIN PROGRAMS
    


star_width = int(input("Please enter an odd number of stars to display in a diamond shape: "))

even = (star_width % 2)
while even == 0:
    print("Please try again")
    star_width = int(input("Please enter an odd number of stars to display in a diamond shape: "))
    even = (star_width % 2)
    
print("Thank you for entering an odd number")
upTriangle()
downTriangle()
     

    
     
     

#center command centers the string based on the first value in the brackets.
#Adding a comma to enter another character fills the outside space with that character.

