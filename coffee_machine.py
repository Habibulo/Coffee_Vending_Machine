from coffee_menu import MENU, resources
profit = 0


def format_data():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f" water left: {water}ml\n milk left: {milk}ml\n coffee left: {coffee}g"


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_money():
    """Returns the total calculated from coins or banknote inserted."""
    total = float(input("how many quarters?: ")) * 0.25
    total += int(input("how many $1 banknote?: ")) * 1
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_title, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_title} ☕️. Enjoy!")


is_on = True
print(" esspresso:  $1.5\n latte:  $2.5\n cappuccino:  $3")
print('we only accept 25cent - [quarter], $1 banknote and 5$ bank notes')
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"{format_data()}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_money()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])