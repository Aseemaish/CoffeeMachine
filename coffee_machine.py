MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}


def take_order():
    print("Welcome to the coffee machine!")
    print("Here are the available options: ")
    print("Espresso: $1.5")
    print("Latte: $2.5")
    print("Cappuccino: $3.0")
    print("Type 'off' to turn off the machine.")
    print("Type 'report' to get the current status of the resources.")
    return "What would you like to order?: "


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(dtt):
    for items in dtt:
        if resources[items] < MENU[order]["ingredients"][items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def calculate_money():
    quarters = int(input("How many Quarters?: "))
    dimes = int(input("How many Dimes?: "))
    nickles = int(input("How many Nickles?: "))
    pennies = int(input("How many Pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def deduct_resources(order):
    resources['water'] -= MENU[order]["ingredients"]["water"]
    resources['coffee'] -= MENU[order]["ingredients"]["coffee"]
    if order != "espresso":
        resources['milk'] -= MENU[order]["ingredients"]["milk"]


while True:
    order = input(take_order())
    if order == "off":
        break
    elif order == "report":
        print_report()
    elif order in MENU:
        choice = MENU[order]
        # check_resources(choice["ingredients"])
        if not check_resources(choice["ingredients"]):
            print("Order cancelled.")
        else:
            money = calculate_money()
            if money >= MENU[order]['cost']:
                deduct_resources(order)
                change = money - MENU[order]['cost']
                profit = MENU[order]['cost']
                change = "{:.2f}".format(change)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif order not in MENU:
        print("Invalid order.")
