'''
FEEL FREE TO COMPLETE THIS CODE IN YOUR OWN TIME :)

Create a simple program that manages a user's order. The program should
prompt the user to:
1. Add something to their cart
2. Display the items in their shopping cart
3. Clear their cart
4. Quit/Exit the order tracker

Create a list called order_tracker to store the items in the user's 
shopping cart.
'''

def take_order(order_tracker, item):
    order_tracker.append(item)

# initialising list 
order_tracker = []

while True:

    print("1. Add something to cart.")
    print("2. Quit.")
    choice = input("What would you like to do?")

    if choice == '1':
        item = input("Enter the item you would like to add: ")
        take_order(order_tracker, item) # function that takes care of adding items to shopping cart

    elif choice == '2':
        print("Exiting.")
        break

    else:
        print("Input invalid. Try again")

# Just checking that the items were successfully added
for item in order_tracker:
    print(item)