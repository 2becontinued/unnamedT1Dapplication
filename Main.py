# Setup!

import datetime

from carbcalculation import carb_calculation
from insulincalculation import insulin_calculation
from clearscreen import clearscreen
from tips import tips
# Setup end!

print("Happy " + datetime.datetime.now().strftime("%A") + "!\n")


# TODO: Put the tips in a separate .py file so its easier to add more tips.

while True:
    print("What would you like to do?\n"
          "1. Calculate carbs.\n"
          "2. Calculate insulin.\n"
          "3. Blood sugar help(Not implemented yet!)\n")
    loop_input = input("INPUT: ").strip().lower()

    if loop_input == "1":
        clearscreen()
        carb_calculation()

    elif loop_input == "2":
        clearscreen()
        insulin_calculation()

    elif loop_input == "3":
        clearscreen()
        pass

    else:
        print("Invalid input, please try again.")
