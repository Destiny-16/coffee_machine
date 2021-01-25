MENU = {
    "espresso": {
        "ingredients": {
            "water": 100,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}


def prompt():
    drink = input("What would you like? (espresso/latte/cappuccino): ")

    # ------------------------ESPRESSO---------------------------------
    if drink == "espresso":

        # WATER CHECK
        water = int(MENU["espresso"]['ingredients']['water'])
        init_water = int(resources["water"])
        final_water = init_water - water

        enough = insufficient_water(water, init_water)
        if enough is False:
            print("Sorry, not enough water.")
            return "on"

        # COFFEE CHECK
        coffee = int(MENU["espresso"]['ingredients']['coffee'])
        init_coffee = int(resources["coffee"])
        final_coffee = init_coffee - coffee

        enough = insufficient_coffee(coffee, init_coffee)
        if enough is False:
            print("Sorry, not enough coffee.")
            return "on"

        total = collect_money(drink)
        successful = transaction_successful(total, drink)
        if not successful:
            return "on"

        resources["water"] = final_water
        resources["coffee"] = final_coffee

    # ------------------------LATTE---------------------------------
    elif drink == "latte":

        # WATER CHECK
        water = int(MENU["latte"]['ingredients']['water'])
        init_water = int(resources["water"])
        final_water = init_water - water

        enough = insufficient_water(water, init_water)
        if enough is False:
            print("Sorry, not enough water.")
            return "on"

        # COFFEE CHECK
        coffee = int(MENU["latte"]['ingredients']['coffee'])
        init_coffee = int(resources["coffee"])
        final_coffee = init_coffee - coffee

        enough = insufficient_coffee(coffee, init_coffee)
        if enough is False:
            print("Sorry, not enough coffee.")
            return "on"

        # MILK CHECK
        milk = int(MENU["latte"]['ingredients']['milk'])
        init_milk = int(resources["milk"])
        final_milk = init_milk - milk

        enough = insufficient_milk(milk, init_milk)
        if enough is False:
            print("Sorry, not enough milk.")
            return "on"

        total = collect_money(drink)
        successful = transaction_successful(total, drink)
        if not successful:
            return "on"

        resources["water"] = final_water
        resources["coffee"] = final_coffee
        resources["milk"] = final_milk

    # ------------------------CAPPUCCINO---------------------------------
    elif drink == "cappuccino":

        # WATER CHECK
        water = int(MENU["cappuccino"]['ingredients']['water'])
        init_water = int(resources["water"])
        final_water = init_water - water

        enough = insufficient_water(water, init_water)
        if enough is False:
            print("Sorry, not enough water.")
            return "on"

        # COFFEE CHECK
        coffee = int(MENU["cappuccino"]['ingredients']['coffee'])
        init_coffee = int(resources["coffee"])
        final_coffee = init_coffee - coffee

        enough = insufficient_coffee(coffee, init_coffee)
        if enough is False:
            print("Sorry, not enough coffee.")
            return "on"

        # MILK CHECK
        milk = int(MENU["cappuccino"]['ingredients']['milk'])
        init_milk = int(resources["milk"])
        final_milk = init_milk - milk

        enough = insufficient_milk(milk, init_milk)
        if enough is False:
            print("Sorry, not enough milk.")
            return "on"

        total = collect_money(drink)
        successful = transaction_successful(total, drink)
        if not successful:
            return "on"

        resources["water"] = final_water
        resources["coffee"] = final_coffee
        resources["milk"] = final_milk

    # TURN OFF MACHINE
    elif drink == "off":
        return "off"

    # GENERATE REPORT
    elif drink == "report":
        for item in resources:
            print(item, ": ", resources[item])

    # INVALID INPUT
    else:
        print("Invalid input. PLease try again.")
        prompt()

    return "on"


def insufficient_water(water, init_water):
    if water > init_water:
        return False


def insufficient_coffee(coffee, init_coffee):
    if coffee > init_coffee:
        return False


def insufficient_milk(milk, init_milk):
    if milk > init_milk:
        return False


def collect_money(drink):
    # quarter = 0.25
    # dime = 0.10
    # nickel = 0.05
    # penny = 0.01

    print("Total is: ", MENU[drink]['cost'])

    num_quarter = int(input("Enter number of quarters: ")) * 0.25
    num_dime = int(input("Enter number of dime: ")) * 0.10
    num_nickel = int(input("Enter number of nickels: ")) * 0.05
    num_penny = int(input("Enter number of pennies: ")) * 0.01

    total = num_quarter + num_dime + num_nickel + num_penny

    return total


def transaction_successful(total, drink):
    paid = float(MENU[drink]['cost'])

    if total < paid:
        print("Sorry that's not enough money. Money refunded.")
        return False

    elif total > paid:
        change = round(total - paid, 2)
        print("Change: $", change)
        resources["profit"] = resources["profit"] + total - change
        print("Here's your ", drink, " Enjoy!")
        return True

    else:
        resources["profit"] = round(resources["profit"] + total, 2)
        print("Here's your ", drink, ", Enjoy!")
        return True


# ---------------------MAIN---------------------------
state = "on"
while state == "on":
    state = prompt()
