import random

welcome_text = "" 
Welcome to the oregon Trail! This year is 1850 and Americans are 
headed out West to populate the frontier. Your goal is to travel 
by wagon train from Independence, MO to Oregon (2000 miles).
You start on March 1st and your goal is to reach Oregon trail by December 31st.
The trail is ardous. Each day costs you food and health. 
You can hunt and rest, but you have to get there before winter! 
""

help_text = ""
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
""

good_luck_text = "Good luck, and see you in Oregon!"

# Modeled Variables 

