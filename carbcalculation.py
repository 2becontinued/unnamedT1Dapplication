# Setup!
from carbfactorlist import carb_factors
from clearscreen import clearscreen


def carb_calculation():
    # setup end!

    while True:  # Main loop
        carb_input = input(
            "What do you plan to eat?\nINPUT: ").strip().lower().replace(" ", "")
        clearscreen()

        # If the carb_input line above's contents are in the list...
        if carb_input in carb_factors:
            try:
                number = carb_factors[carb_input]  # Store the carb factor!
            except ValueError:
                print("Sorry, thats not a number. Try once more!")
                continue
            # Then say it, of course.
            print("The carb factor for " + carb_input + " is: " + str(number))

            calculation_input = input(
                "Would you like to calculate the carbs for it based of grams? Y/N\nINPUT: ").strip().lower()
            # Adding a clearscreen() here doesnt work for whatever unknown reason.
            # Also every file in pycharm is red but works flawlessly
            # im scared.
            if calculation_input == "y":  # If calculation_input = Y..
                clearscreen()
                calculation_math_input = input(
                    "How many grams do you have?\n").strip()

                calculation_input = int(calculation_math_input)  # i remember putting a try here for errors..
                                                                 # oh well ill fix it eventually
                calculation_result = calculation_input * number

                print(
                    "The calculated carbs are: " +
                    str(calculation_result))

                print("Have a good day!")
                break

            else:
                print("Interpreting answer as no.\nHave a good day!")
                break

        else:
            print("""
            Not found in the list, please put it in differently,
            if rephrasing it doesnt work, create a issue on the github page
            and I will fix it as soon as possible.
            """)
            continue
