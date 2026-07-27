# Access your data
# print(product_data)

#1. Load product data from JSON file
# import json
# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "MyFile.json")

# with open(file_path, "r", encoding="utf-8-sig") as file:
#     data = json.load(file)

# # print(data)
# for item_dict in data:
#     # Get only the values from the current dictionary
#     item_values = list(item_dict.values())
#     print(item_values)

#2.Modify login to handle incorrect input via exceptions


# try:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if not username or not password:
#         raise ValueError("Username or password cannot be empty.")

#     valid_username = "Harry Potter"
#     valid_password = "123456"

#     if username == valid_username and password == valid_password:
#         print("Login Successful!")
#     else:
#         raise PermissionError("Invalid username or password.")

# except ValueError as ve:
#     print("Input Error:", ve)

# except PermissionError as pe:
#     print("Permission Error:", pe)

# except Exception as e:
#     print("Unexpected Error:", e)



#3.  Build Login class with validation method

# class Login:
#     def __init__(self, user_name, password):
#         self.username = user_name
#         self.password = password

#     def validation(self):
#         valid_user = "Harry Potter"
#         valid_pass = "123456"

#         if self.username == valid_user and self.password == valid_pass:
#             print("Login Successful")
#         else:
#             print("Invalid Username or Password")


# # User Input
# user_name = input("Enter Username: ")
# password = input("Enter Password: ")

# # Create object
# obj = Login(user_name, password)

# # Call validation method
# obj.validation()

# 4.  Create reusable login module

# import Login as login_module

# uname = input("Enter Username: ")
# pwd = input("Enter Password: ")

# if login_module.login(uname, pwd):
#     print("Login Successful")
# else:
#     print("Invalid Username or Password")


# 5. Call GET API and print response



# import requests

# # API URL
# url = "https://jsonplaceholder.typicode.com/posts/1"

# # Send GET request
# response = requests.get(url)

# # Check status code
# if response.status_code == 200:
#     print("Response:")
#     print(response.json())  # Print JSON response
# else:
#     print("Error:", response.status_code)

#6.  Filter products with price < 50


# List of products
# products = [
#     {"name": "Pen", "price": 10},
#     {"name": "Notebook", "price": 60},
#     {"name": "Pencil", "price": 5},
#     {"name": "Bag", "price": 100}
# ]

# # Filter products with price < 50
# filtered_products = [product for product in products if product["price"] < 50]

# # Print filtered products
# for product in filtered_products:
#     print(product)

import json
import os
import Login as login_module

uname = input("Enter Username: ")
pwd = input("Enter Password: ")

if login_module.login(uname, pwd):
    print("Login Successful")
else:
    print("Invalid Username or Password")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "MyFile.json")

with open(file_path, "r", encoding="utf-8-sig") as file:
    data = json.load(file)

# print(data)
print("The items in your cart are:")
for item_dict in data:
    # Get only the values from the current dictionary
    item_values = list(item_dict.values())
    print(item_values)
