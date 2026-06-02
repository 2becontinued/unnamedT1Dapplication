def insulin_calculation():
    while True:
        carb_input = input(
            "Please enter your carbs.\nINPUT: ").strip().lower()

        try:
            carb = float(carb_input)
        except ValueError:
            print("What you inputted appears to be invalid. Try again.")
            continue

        insulin_input = input(
            "Please enter your insulin to carb ratio.\nINPUT: ").strip().lower()

        try:
            insulin_ratio = float(insulin_input)
        except ValueError:
            print("What you inputted appears to be invalid. Try again.")
            continue

        result = carb / insulin_ratio

        print("The calculated insulin is: " + str(result))
        print("Have a good day!")
        break
