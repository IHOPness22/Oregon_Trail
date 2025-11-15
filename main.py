import random

welcome_text = """ 
Welcome to the oregon Trail! This year is 1850 and Americans are 
headed out West to populate the frontier. Your goal is to travel 
by wagon train from Independence, MO to Oregon (2000 miles).
You start on March 1st and your goal is to reach Oregon trail by December 31st.
The trail is ardous. Each day costs you food and health. 
You can hunt and rest, but you have to get there before winter! 
"""

help_text = """"
Each turn you can take one of 3 actions

 travel - moves you randomly between 30-60 miles and 
	takes 
		3-7 days (random)
	rest
		increases health 1 level (up to 5 maximum) and 
	takes 
		2-5 days (random)
	hunt 
		adds 100 lbs of food and takes 2-5 days (random)
When prompted for an action, you can also enter one of these commands without
 using your turn: 

	status - lists food, health, distance traveled, and day.
	help - list all the commands 
	quit - will end the game 

You can also use shortcuts for commands:

	't', 'r', 'h', 's', 'q'
"""

good_luck_text = "Good luck, and see you in Oregon!"

# Modeled Variables 

miles_traveled = 0
food_remaining = 500
health_level = 5
month = 3
day = 1
year = 1848
sickness_suffered_this_month = 0
player_name = None

#Constants -- input which don't change

MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

FOOD_PER_HUNT = 100 
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 5
MILES_BETWEEN_NYC_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
	'fake', 'January', 'February', 'March', 'April', 'May',
	'June', 'July', 'August', 'September', 'October',
	'November', 'December'
]

#Converts are numeric data into a string 
# input: m - a month in the range 1-12
# input: d - a day in the range 1-31
# output: A string like "December 24"
#This function does not reinforce calender rules, it's happy to output 
#impossible strings like "June 95" or "February 31"

#-----------------------FUNCTIONS-------------------------

def date_as_string(m):
    return NAME_OF_MONTH[m]
	

def date_report():
	#Enter code here 
	pass

def miles_remaining():
	#Enter code here
	pass

#Return the number of days in a month (28, 30 or 31).
#input: an integer from 1-12. 1=January, 2=february, etc
#output: the number of days in a month. If the input is not in 
#the required range returns 0

def days_in_months(m,d):
    if m in MONTHS_WITH_31_DAYS and d > 31:
        m += 1 	
        d = 1
    elif m in MONTHS_WITH_30_DAYS and d > 30:
        m += 1
        d = 1
    elif m in MONTHS_WITH_28_DAYS and d > 28:
        m += 1
        d = 1

    if m > 12:
        m = 1
    return m,d


#Calculates when a sickness occurs on the current day based
# on how many days remain in the month and how many sick days have
#already occured in the month, then 
#the chance of a sick day is either 0, 1, out of N or 2 out of N
#depending on how many sick days there been so far 

#The system guarentees that there will be exactly 2 sick days in the month
# and incidentally every day of the month 

def random_sickness_occurs():
	#Enter your code here
	pass

def handle_sickness():
	#Enter your code here
	pass

def consume_food():
	#Enter your code here 
	pass

#Repairs problematic value in the global (month, day)
#model where the day is 
#larger than the number of the month, If this happens
#advance to the next
#month and knocks down the day back to 1
#Returns true if the global month/day were altered, else false.

def maybe_rollover_month():
	#enter your code here 
	pass

#Causes certain days to elapse. The days pass one at a time, and each
#day brings a random chance of sickness. The sickness rules are quirky:
#player
#is guarenteed to fall ill a certain number of times a month, so illness
#needs to keep track of month changes 
#
# input: num_days - an integer number of days that elapse

def advance_game_clock(num_days):
	#Enter your code here
	pass


#--------------------------Handlers-------------------------
def handle_choice(choice):
    if choice == "1":
        handle_travel()
    elif choice == "2":
        handle_rest()
    elif choice == "3":
        handle_hunt()
    else:
        print("invalid input, try again")
        new_choice = player_input()
        handle_choice(new_choice)

def handle_travel():
    global miles_traveled
    global day
    global month
    global food_remaining
    miles_traveled += 30
    day += 1
    food_remaining -= 30
    month, day = days_in_months(month, day)
    game_loop()

def handle_hunt():
	#Enter your code here
	pass

def handle_status():
	#Enter your code here
	pass

def handle_help():
	#Enter your code here
	pass

def handle_quit():
	global playing 
	playing = False

def handle_invalid_input(response):
	pass

def game_is_over():
	#Enter your code here 
	pass

def player_wins():
	#Enter your code here 
	pass

def loss_report():
	#Enter your code here
	pass


#-------------------Game loops----------------
def init_game():
    global miles_traveled, food_remaining, health_level
    global month, day, sickness_suffered_this_month, player_name
    global year

    # Reset modeled variables
    miles_traveled = 0
    food_remaining = 500
    health_level = 5
    month = 3        # March
    day = 1          # 1st day of the month
    year = 1848
    sickness_suffered_this_month = 0
    player_name = None

def beggining_text():
    print(welcome_text + help_text + good_luck_text)
    input("Press Enter to continue")
    global player_name
    player_name = input("What is your name player? ")
    	
def game_loop():
    menu()
    choice = player_input()
    handle_choice(choice)

def menu():
    print("------------------------------------------")
    print(f"Date: {date_as_string(month)} {day}, {year}")
    print("Weather: hot")
    print("Health: fair")
    print(f"Food: {food_remaining}")
    print(f"Miles traveled {miles_traveled}")
    print("------------------------------------------")    

def player_input():
    print(f"What would you like to do {player_name}....")
    print("1. Travel")   
    print("2. Rest")
    print("3. Hunt")
    choice = input("Choose your option: ")   
    return str(choice) 

def main():
    init_game()
    beggining_text()
    game_loop()



if __name__ == "__main__":
    main()
