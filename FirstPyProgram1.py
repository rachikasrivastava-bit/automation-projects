#Assignment 1 :  
 	
# 1. Install Python & check version
# 2. Print name, age, boolean
# 3. Create username & password variables  	
# 4. Store product list using Python list
# 5. Build login validation (valid vs invalid credentials)

# is_adult = True                           #2 Print name, age, boolean
# name = input("Enter your name: ")
# print("Hello, " + name)
# age = input("Enter your age: ")
# print("You are " + age + " years old.")

# if float(age) < 18:
#     is_adult = False
#     print("You are not an adult.")
# else:
#     print("You are an adult.")


#     user_name = input("Enter your username: ")               #3 Create username & password variables
# password = input("Enter your password: ")
# if user_name == "Rachika" and password == "123456":
#     print("You are successfully logged in!")
# else:
#     print("Invalid username or password. Please try again.")

# furniture_store_product_list = ["\n" "Chair", "\n", "Coffee Table", "\n", "Couch", "\n", "Recliner", "\n", "Side tables"]     #4 Store product list using Python list
# print("The available products in store are :")
# for item in furniture_store_product_list:
#     print(item)



# user_name = input("Enter your username: ")               #5. Build login validation (valid vs invalid credentials)
# password = input("Enter your password: ")
# if user_name == "Rachika" and password == "123456":
#     print("You are successfully logged in!")
# else:
#     print("Invalid username or password. Please try again.")


# wall_paint_brands = ["\n" "Asian Paints", "\n", "Berger", "\n", "Dulux", "\n", "Nerolac"]     #6. Loop through product list and print each item  
 	
# print("The best wall paints are :")
# for item in wall_paint_brands:
#     print(item)

user_name = input("Enter your user name: ")               #7 Create login function with parameters; return success/failure
password = input("Enter your password: ")
def Fn_login(user_name, password):
    if user_name == "Happy@Singh" and password == "happy123":
        print("Successful login!")
        return True 
    else:
        print("Invalid user name or password. Please try again.")
        return False
        
login_status = Fn_login(user_name, password)        