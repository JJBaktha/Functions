#Jeeson Baktha
#Function Revision 1
#27 November 2014


#FUNCTIONS

def userInput():
    symbol = input("Please enter a symbol")
    repeats = int(input("Please enter the amount of times to repeat the symbol"))
    return symbol, repeats

def OutPutSymbols(symbol, repeats):
     for count in range(repeats):
         print(symbol)

#MAIN PROGRAMS

symbol, repeats = userInput()
OutPutSymbols(symbol, repeats)
