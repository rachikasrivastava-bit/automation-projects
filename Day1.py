#Assignment 1 :  
 	
# 1. Install Python & check version
# 2. Print name, age, boolean
# 3. Create username & password variables  	
# 4. Store product list using Python list
# 5. Build login validation (valid vs invalid credentials)

is_adult = True                           #2 Print name, age, boolean
name = input("Enter your name: ")
print("Hello, " + name)
age = input("Enter your age: ")
print("You are " + age + " years old.")

if float(age) < 18:
    is_adult = False
    print("You are not an adult.")
else:
    print("You are an adult.")

#===========================================================================

    user_name = input("Enter your username: ")               #3 Create username & password variables
password = input("Enter your password: ")
if user_name == "Rachika" and password == "123456":
    print("You are successfully logged in!")
else:
    print("Invalid username or password. Please try again.")


#===========================================================================

# Store product list using Python list
furniture_store_product_list = ["\n" "Chair", "\n", "Coffee Table", "\n", "Couch", "\n", "Recliner", "\n", "Side tables"] 
print("The available products in store are :")
for item in furniture_store_product_list:
    print(item)



user_name = input("Enter your username: ")               #5. Build login validation (valid vs invalid credentials)
password = input("Enter your password: ")
if user_name == "Rachika" and password == "123456":
    print("You are successfully logged in!")
else:
    print("Invalid username or password. Please try again.")


wall_paint_brands = ["\n" "Asian Paints", "\n", "Berger", "\n", "Dulux", "\n", "Nerolac"]     #6. Loop through product list and print each item  
 	
print("The best wall paints are :")
for item in wall_paint_brands:
    print(item)

user_name = input("Enter your user name: ")               #7 Create login function with parameters; return success/failure
password = input("Enter your password: ")
def Fn_login(user_name, password):
    if user_name == "Happy@Singh" and password == "happy123":
        print("Successful login!")
        return True 
    else:
        print("Invalid user name or password. Please try again!")
        return False
        
login_status = Fn_login(user_name, password) 


##======================================================================

class  Product:               #Day1: Create product objects (id, name, price) and access values
# 1. Initializing id, name, and price
    def __init__(self, itemID, itemName, itemPrice):
        self.id = itemID
        self.name = itemName
        self.price = itemPrice

 # 2. Display product details
    def display(self):
        return f"Product [{self.id}]: {self.name} costs Rs.{self.price:.2f}"

# 3. Creat product objects
prod1 = Product("I01", "Chair", 199.99)
prod2 = Product("I02", "Coffee Table", 299.99)
prod3 = Product("I03", "Couch", 499.99)
prod4 = Product("I04", "Lampshade", 99.99)

# 4. Access values via a class method
print("\n--- Accessing Values ---")
print(prod1.display())
print(prod2.display())
print(prod3.display())
print(prod4.display())


##======================================================================

is_loggedin = False
user_name = input("Enter your username: ")
password = input("Enter your password: ")
if user_name == "Harry Potter" and password == "123456":
    is_loggedin = True
    print("You are successfully logged in!")
else:
    print("Invalid username or password. Please try again.")

if is_loggedin:
    print("You are logged in. Go to your cart and check out.")
    furniture_store_product_list = ["Chair", "Coffee Table", "Couch", "Recliner"]
    print("Items in your cart :")
    for cartitem in furniture_store_product_list:
        print(cartitem)
else:
    print("You are not logged in. Please log in to view your cart.")

choice = input("Do you want to checkout? (yes/no): ")
if choice.lower() == "yes":
    print("Thank you for your purchase!")   