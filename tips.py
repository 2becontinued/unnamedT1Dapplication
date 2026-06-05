# Setup!

import random

# Setup end!

def tips():  # The whole point of the file.

    random_tip = random.randint(1, 11)  # Get a random int number, and depending on what it is, print something.

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
        (print
         ("Random tip: These tips are from personal experience.\n"))

    elif random_tip == 7:
        print(
            "Random tip: Showers can dip blood sugars on CGMs.\n")

    elif random_tip == 8:
        print(
            "Random tip: Alternate between spots for injection and insulin pump sites!\n")

    elif random_tip == 9:
        print(
            "Random tip: It is recommended to disinfect the area you put in a CGM or insulin pump site.\n")

    elif random_tip == 10:
        print(
            "Random tip: Some food can have a different carb factor depending on how they were cooked!\n")

    elif random_tip == 11:
        print(
            "Random tip: If your blood sugar is low, it is recommended to reduce insulin a bit if your dosing for food.\n")

    elif random_tip == 12:
        print(
            "Random tip: Exercising while having a blood sugar less then 5 whilst having insulin on board will result in a low blood sugar.\n")

# Eventually I plan on having around 20 tips, but for now this will do