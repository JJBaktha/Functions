#Jeeson Baktha
#Function Revision 3
#25 November 2014

#FUCNTIONS

def sort(x, y):
   if x > y:
      print(x, "is bigger than", y)
   else:
      print(y, "is bigger than",
            x)
         


#MAIN PROGRAMS

print("This program will sort two numbers you enter into order.")
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))



sort(x, y)
