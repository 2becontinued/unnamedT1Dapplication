# Setup!

import datetime
import random

from carbcalculation import carb_calculation
from insulincalculation import insulin_calculation
from clearscreen import clearscreen
# Setup end!

print("Happy " + datetime.datetime.now().strftime("%A") + "!\n")

random_tip = random.randint(1, 8)

if random_tip == 1:
    print(
        "Random tip: Treating a low blood sugar with sugary sodas such as mountain dew is better then using most candys.\n")

elif random_tip == 2:
    print("Random tip: Use alcohol when your blood testing!\n")

elif random_tip == 3:
    print(
        "Random tip: A blood sugar above 13 mmol/L can affect your mood drastically. Plan social events accordingly!\n")

elif random_tip == 4:
    print(
        "Random tip: A low blood sugar can affect you drastically, pale lips is a sign that your low. Shaking of the fingers also is a sign.\n")

elif random_tip == 5:
    print(
        "Random tip: If you have have a lingering pain from a slap, a insulin injection is likely to not hurt as much.\n")

elif random_tip == 6:
    print("Random tip: These tips are from personal experience.\n")

elif random_tip == 7:
    print("Showers can dip blood sugars on CGMs.\n")

elif random_tip == 8:
    print("Alternate between spots for injection and insulin pump sites!\n")


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
