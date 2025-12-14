import sys
import random
from dataclasses import dataclass

welcome_text = """ 
Welcome to the oregon Trail! This year is 1850 and Americans are 
headed out West to populate the frontier. Your goal is to travel 
by wagon train from Independence, MO to Oregon (2000 miles).
You start on March 1st and your goal is to reach Oregon trail by December 31st.
The trail is ardous. Each day costs you food and health. 
You can hunt and rest, but you have to get there before winter! 
"""

help_text = """
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
sick_counter = 1
player_name = None
health_bar = 100

#Constants -- input which don't change

MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 45
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5
SICK_CHANCE = 0.03
RECOVERY_CHANCE = 0.10
SHALLOW_ODDS_1 = 0.6
SHALLOW_ODDS_2 = 0.4
SHALLOW_ODDS_3 = 0.2 
SHALLOW_ODDS_4 = 0

FOOD_PER_HUNT = 100 
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 30
MILES_BETWEEN_NYC_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]
SICKNESS = ["Cholera", "Dysentery", "Measles", "Typhoid", "Fever"]
WEATHER = ["Sunny", "Hot", "Cloudy", "Rain", "Thunderstorms"]
WINTER_WEATHER = ["Snow"]
SUMMER_WEATHER = ["Hot"]
CURRENT_WEATHER = 0
WEATHER_SPEED = 0

@dataclass
class River:
    name: str
    distance: int
    depth: float 
    width: int 
    ferry_cost: int
    has_ferry: bool
    river_passed: bool = False

rivers = [
    River("Kansas River", 102, round(random.uniform(1,7),1), 200, 5, True),
    River("Big Blue River", 185, round(random.uniform(1,7),1),240, 3, False),
    River("Snake River", 1200, round(random.uniform(1,7),1),430, 8, True)
]

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

#------------------READABLE STRINGS-------------------------

def date_as_string(m):
    return NAME_OF_MONTH[m]

def miles_remaining():
    miles_remained = MILES_BETWEEN_NYC_AND_OREGON - miles_traveled
    return miles_remained


#------------------STARVATION--------------------------------

def starve_effect():
    global food_remaining
    global health_bar
    if food_remaining <= 0:
        food_remaining = 0
        health_bar -= random.randint(1,10)     
        print("Your starving, you need more food")

#Return the number of days in a month (28, 30 or 31).
#input: an integer from 1-12. 1=January, 2=february, etc
#output: the number of days in a month. If the input is not in 
#the required range returns 0

#----------------------MAKES DAY SYSTEM FEEL LIKE A CALENDER--------------

def days_in_months(m,d):
    if m in MONTHS_WITH_31_DAYS and d > 31:
        m += 1 	
        d = d - 31
    elif m in MONTHS_WITH_30_DAYS and d > 30:
        m += 1
        d = d - 30
    elif m in MONTHS_WITH_28_DAYS and d > 28:
        m += 1
        d = d - 28
    if m > 12:
        m = 1

    return m,d

def max_days_per_month(m):
    if m in MONTHS_WITH_31_DAYS:
        p = 31
    elif m in MONTHS_WITH_30_DAYS:
        p = 30
    elif m in MONTHS_WITH_28_DAYS:
        p = 28
    return p

#------------------SPAWN SICKNESS AND HANDLE-------------------------

def random_sickness_occurs():
    global SICK_CHANCE
    global health_status

    if health_status == "Healthy":
        if random.random() <= SICK_CHANCE:
            health_status = random.choice(SICKNESS)
            input(f"You have {health_status}")
            return health_status


def handle_sickness():
    global sick_counter
    global health_status
    if health_status != "Healthy":
        DISEASE_BEHAVIOR[health_status]()
        if random.random() <= RECOVERY_CHANCE * sick_counter:
            input(f"You recovered from {health_status}")
            sick_counter = 1
            health_status = "Healthy"
            return health_status
        else:
            sick_counter += 1

#----------------------------DISEASE FUNCTIONS--------------------
def cholera_effect():
    global health_bar 
    health_bar -= random.randint(5,15)

def dysentery_effect():
    global health_bar
    health_bar -= random.randint(5,20)

def measles_effect():
    global health_bar
    health_bar -= random.randint(5,15)

def typhoid_effect():
    global health_bar
    health_bar -= random.randint(5,15)
 
def fever_effect():
    global health_bar 
    health_bar -= random.randint(1,10)


#Dictionary is below functions so that the fuctions are initialized
#-------------------------DISEASE DICTIONARY------------------------
DISEASE_BEHAVIOR = { 
    "Cholera": cholera_effect,
    "Dysentery": dysentery_effect,
    "Measles": measles_effect,
    "Typhoid": typhoid_effect,
    "Fever": fever_effect
} 

#-------------------------SLEEP_EFFECTS-----------------------------
def rest_status():
    global health_bar
    global health_status
    global sleep_days
    global day
    day += sleep_days
    if health_bar == 100:
         print(f"You have slept for {sleep_days} days")
    else:
        new_health = 3 * sleep_days
        health_bar += new_health
        print(f"You slept for {sleep_days} and gained {new_health}HP") 
        if health_bar >= 100:
             health_bar = 100
    if health_status != "Healthy":
        if random.random() <= RECOVERY_CHANCE * sleep_days:
            input(f"You recovered from {health_status}")
            health_status = "Healthy"
            return health_status
    
        
def rest_option():
    global sleep_days
    while True:
        try:
            sleep_days = int(input("How many days to hit the hay... (2-5)"))
            if sleep_days >= 2 and sleep_days <= 5:
                break
            else:
                print("Pick a number between 2 and 5")
        except ValueError:
            print("Invalid input")  

#---------------------------RIVER CHECK---------------------------
def river_check():
    global miles_traveled 
    for river in rivers:
        if miles_traveled >= river.distance and river.river_passed == False:
            input(f"You are now at {river.name}!")
            choice = river_menu(river)
            handle_river_choice(choice, river)
            river.river_passed = True

def ferry_avail(river):
    if river.has_ferry == True:
        return "Present"
    else:
        return "Absent"

#---------------------------RIVER MENU-----------------------------
def river_menu(river):
    print(f"Width: {river.width}ft")
    print(f"Depth: {river.depth}ft")
    print(f"Weather: {CURRENT_WEATHER}")
    print(f"Ferry availability: {ferry_avail(river)}")
    print("\n")
    print("You may: \n")
    print("1. Attempt to ford the river")
    print("2. Caulk the wagon and float it across")
    print("3. Take a ferry")
    print("4. Wait to see if conditions imporve")
    river_choice = int(input("What would you like to do (1-4)"))
    return river_choice
    
#--------------------------RIVER HANDLER-------------------------
def handle_river_choice(river_choice, river):
    if river_choice == 1:
        input("Ok here we go....")
        ford_river(river)
    elif river_choice == 2:
        input("Ok here we go....")
        caulk_river(river)
    elif river_choice == 3:
        input("Ok ferry it is...")
        take_ferry(river)
    elif river_choice == 4:
        input("Ok lets wait...")
        wait_river(river)
    else:
        print("Invalid input")
        new_choice = river_menu(river)
        handle_river_choice(new_choice, river)

#---------------------------RIVER FUNCTIONS--------------------------
def ford_river(river):
    global food_remaining
    global day 
    if river.width <= 3:
        river_odds = SHALLOW_ODDS_1
    elif river.width > 3 and river.width <= 4:
        river_odds = SHALLOW_ODDS_2
    elif river.width > 4 and river.width <= 5:
        river.odds = SHALLOW_ODDS_3
    else:
        river_odds = SHALLOW_ODDS_4
    
    if random.random() <= river_odds:
        print("You have succesfully crossed the river!")
        input("No damages!")
    else:
        print("Your boat was damaged in the process")
        input("lost 10 days repairing and lost food")
        day += 10 
        food_remaining -= random.randint(60,120)
        starve_effect()

        

        


def caulk_river(river):
    #Enter your code here
    pass

def take_ferry(river):
    #Enter your code here
    pass

def wait_river(river):
    #Enter your code here 
    pass

#------------------------HANDLE WEATHER-------------------------
def get_weather_string():
    return random.choice(WEATHER)

def get_winter_string():
    return random.choice(WINTER_WEATHER)

def get_summer_string():
    return random.choice(SUMMER_WEATHER)

def start_weather():
    global CURRENT_WEATHER
    global month
    global WEATHER_SPEED
    global SICK_CHANCE
    if month not in (12, 1, 2, 6, 7):
        CURRENT_WEATHER = get_weather_string()
        if CURRENT_WEATHER == "Hot":
            WEATHER_SPEED = -2
            SICK_CHANCE = 0.035
        elif CURRENT_WEATHER == "Sunny":
            WEATHER_SPEED = 0
            SICK_CHANCE = 0.02
        elif CURRENT_WEATHER == "Cloudy":
            WEATHER_SPEED = 0
            SICK_CHANCE = 0.03
        elif CURRENT_WEATHER == "Rain":
            WEATHER_SPEED = -3
            SICK_CHANCE = 0.04 
        elif CURRENT_WEATHER == "Thunderstorms":
            WEATHER_SPEED = -5
            SICK_CHANCE = 0.04   
    #finish the weather 
    elif month in (12, 1, 2):
        CURRENT_WEATHER = get_winter_string()
        SICK_CHANCE = 0.099
        WEATHER_SPEED = -random.randint(10, 20)

    elif month in (6, 7):
        CURRENT_WEATHER = get_summer_string()
        SICK_CHANCE = 0.035
        WEATHER_SPEED = -2

           

    







    


#-------------------------GAME HANDLERS-------------------------

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
    global MIN_MILES_PER_TRAVEL
    global MAX_MILES_PER_TRAVEL
    global days_per_month
    global miles_traveled
    global day
    global month
    global food_remaining
    miles_traveled += random.randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)
    added_day = random.randint(1,3)
    day += added_day
    food_remaining -= FOOD_EATEN_PER_DAY * added_day 
    month, day = days_in_months(month, day)
    days_per_month = max_days_per_month(month)
    start_weather() #e
    random_sickness_occurs()
    handle_sickness()
    starve_effect()
    loss_report()
    river_check()
    

def handle_hunt():
    global month
    global food_remaining
    global day
    global days_per_month
    global health_status
    input("Ready to hunt... press your luck")
    food_gained = random.randint(30, 100)
    days_lost = random.randint(2, 5)
    day += days_lost
    random_sickness_occurs()
    handle_sickness()
    loss_report()
    month, day = days_in_months(month, day)
    days_per_month = max_days_per_month(month)
    food_remaining += food_gained
    print(f"You gained {food_gained} food")
    input(f"But you lost..... {days_lost} days")

def handle_rest():
    global month
    global food_remaining
    global day 
    global days_per_month
    global sleep_days
    rest_option()
    rest_status()


def handle_status():
	pass

def handle_help():
	print(help_text)

def handle_quit():
	global playing 
	playing = False

def handle_invalid_input(response):
	pass

def game_is_over():
	sys.exit(0)

def player_wins():
	#Enter your code here 
	pass

def loss_report():
    global health_bar
    if health_bar <= 0: 
        health_bar = 0 
        print("You died, Try again")
        game_is_over()


#-------------------Game loops----------------
def init_game():
    global miles_traveled, food_remaining, health_level
    global month, day, player_name
    global year, days_per_month, health_status, health_bar
    global sick_counter, sleep_days

    # Reset modeled variables
    miles_traveled = 0
    food_remaining = 500
    health_level = 5
    month = 3        # March
    day = 1          # 1st day of the month
    year = 1848
    days_per_month = 0
    player_name = None
    health_status = "Healthy"
    health_bar = 100
    sick_counter = 1
    sleep_days = 1

def beggining_text():
    print(welcome_text + help_text + good_luck_text)
    input("Press Enter to continue")
    global player_name
    player_name = input("What is your name player? ")
    	
def game_loop():
    while True:
        menu()
        choice = player_input()
        handle_choice(choice)

def menu():
    print("------------------------------------------")
    print(f"Date: {date_as_string(month)} {day}, {year}")
    print(f"Weather: {CURRENT_WEATHER}")
    print(f"Food: {food_remaining}")
    print(f"Miles traveled {miles_traveled}")
    print("------------------------------------------")    
    print(f"HP:{health_bar}")

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
