
import Login as login_module

uname = input("Enter Username: ")
pwd = input("Enter Password: ")

isLoggedin = login_module.login(uname, pwd)
if isLoggedin:
    print("Login Successful")
else:
    print("Invalid Username or Password")
if isLoggedin:
    # Product List

    products = {
        1: {"name": "Chair", "price": 5000},
        2: {"name": "Table", "price": 8000},
        3: {"name": "Lampshade", "price": 2500},
        4: {"name": "Bean Bag", "price": 1500}
    }

    cart = []

    # Display Products
    print("Available Products:")
    for pid, product in products.items():
        print(f"{pid}. {product['name']} - Rs.{product['price']}")

    # Add Products to Cart
    while True:
        try:
            choice = int(input("\nEnter Product ID to add to cart (0 to checkout): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break

        if choice in products:
            cart.append(products[choice])
            print(products[choice]["name"], "added to cart.")
        else:
            print("Invalid Product ID!")

    # Checkout Logic
    print("\n----- CART -----")
    total = 0

    for item in cart:
        print(f"{item['name']} - Rs.{item['price']}")
        total += item["price"]

    print("----------------")
    print("Total Amount: Rs.", total)
    print("Checkout Successful!")