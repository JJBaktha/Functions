#Jeeson Baktha
#Function Stretch and challenge 2
#4 December 2014




import random

def counter():
    counter_input = int(input("Please enter tha mount of counters you want to user (10-50): "))
    
    while counter_input < 10 or counter_input > 50:
        print("That is not between 10 and 50 sorry. Try again.")
        counter_input = int(input("Please enter the amount of counters you want to use (10-50)"))
    no_counters = counter_input
    return no_counters


def user_turn(no_counters):
    print("Your Turn")
    user_counters = int(input("How many counters do you want to take? (you can take up to 3)"))
    while user_counters <1 or user_counters > 3:
        print("That is not between 1 and 3. Try again")
        user_counters = int(input("How many counters do you want to take?\n"))
    no_counters = no_counters - user_counters
    print("There are {0} counters left".format(no_counters))
    return no_counters

def computer_turn(no_counters):
    print("Computers Turn")
    computer_counters = random.randint(1,3)
    no_counters = no_counters - computer_counters
    print("The computer has taken {0} counters".format(computer_counters))
    print("There are {0} counters left".format(no_counters))
    return no_counters


#MAIN PROGRAM
no_counters = counter()
turn = "user"
while no_counters > 5:
    if turn == "user":
        no_counters = user_turn(no_counters)
        turn = "com"
    elif turn == "com":
        no_counters = computer_turn(no_counters)
        turn = "user"


