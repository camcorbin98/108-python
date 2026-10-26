from catalog import store_items

cart = []

def header(text):
    print("--------------------")
    print(text)
    print("--------------------")


def menu():
    print("Menu")
    print("1.- View Catalog")
    print("2.- Search Product")
    print("3.- View Cart")
    print("Q.- Quit")


def print_catalog():
    header("- Our Catalog")

    for prod in store_items:
        print(f' | {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')

    answer = input("Type ID to add (N to close): ")

    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)


def add_product_to_cart(prod_id):
    found = False

    for prod in store_items:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)
            print(f'{prod["title"]} added to your cart.')
            break

    if not found:
        print("ERROR: Invalid ID")


def search_product():
    text = input("Search Title: ").lower()
    found = False

    for prod in store_items:
        if text in prod["title"].lower():
            found = True

            print(f'Found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]:.2f}')

            choice = input("Do you want to add this item to your cart? (y/n): ")

            if choice.lower() == "y":
                add_product_to_cart(prod["id"])

            break

    if not found:
        print("Sorry, this item doesn't exist.")


def view_cart():
    # 1. Print header "Your Cart"
    header("Your Cart")

    # 2. Check if cart is empty
    if len(cart) == 0:
        print("Your cart is empty.")

    # 3. Otherwise, display all items in cart
    else:
        for prod in cart:
            print(f' | {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')


options = ""

while options != "q" and options != "Q":
    header("Welcome to Store X")
    menu()

    options = input("Choose an option: ")

    if options == "1":
        print_catalog()

    elif options == "2":
        search_product()

    elif options == "3":
        view_cart()

    elif options == "q" or options == "Q":
        print("Good Bye!")
        break

    else:
        print("Invalid option. Please try again.")