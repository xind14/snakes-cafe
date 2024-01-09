def print_menu():
    menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **    
***********************************"""
    print(menu)



def order():
    orders = {}
    while True:
        user_order = input(">")
        if user_order.lower() == "quit":
            break

        if user_order.lower() in ["wings", "cookies", "spring rolls", "salmon", "steak", "meat tornado", "a literal garden", "ice cream", "cake", "pie", "coffee", "tea", "unicorn tears"]:
            if user_order in orders:
                orders[user_order] += 1
            else:
                orders[user_order] = 1
            order_count = orders[user_order]
            order_plural = 'orders' if order_count != 1 else 'order'
            has_have = 'have' if order_count != 1 else 'has'
            print(f"\n** Thanks for ordering! **")
            print(f" ** {order_count} {order_plural} of {user_order} {has_have} been added to your meal **\n")
            print("** Would you like to order anything else? **\n")
        else:
            print("\nSorry, that item is not on the menu. Please choose something from the menu.\n")

    print("\n=== Summary of Your Order ===")
    for item, count in orders.items():
        print(f"{count} {item}")
    print("=============================")
    print("Thank you for ordering. Come again.")
    
print_menu()
order()

