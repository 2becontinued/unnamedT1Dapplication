# Setup!
from carbfactorlist import carb_factors
from clearscreen import clearscreen


def carb_calculation():
    # setup end!

    while True:

        carb_input = input(
            "What do you plan to eat?\nINPUT: ").strip().lower().replace(" ", "")
        clearscreen()

        # If the carb_input line above's contents are in the list...
        if carb_input in carb_factors:

            number = carb_factors[carb_input]  # Store the carb factor!

            # Then say it, of course.
            print("The carb factor is: " + str(number))

            calculation_input = input(
                "Would you like to calculate the carbs for it based of grams? Y/N\nINPUT: ").strip().lower()

            # Adding a clearscreen() here doesnt work for whatever unknown reason.
            if calculation_input == "y":  # If calculation_input = Y..

                clearscreen()
                calculation_math_input = input(
                    "How many grams do you have?\n").strip()

                try:
                    calculation_input = int(calculation_math_input)
                except ValueError:  # If there were letters instead of numbers...
                    print("Sorry, thats not a number. Try once more!")  # Print a little error message
                    continue # And loop!

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
            print(
            "Not found in the list, please put it in differently,"
            "if rephrasing it doesnt work, create a issue on the github page"
            "and I will fix it as soon as possible."
            )
            continue


    # TODO: Figure out how to make the search better.