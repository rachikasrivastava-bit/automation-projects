is_adult = True
name = input("Enter your name: ")
print("Hello, " + name)
age = input("Enter your age: ")
print("You are " + age + " years old.")

if float(age) < 18:
    is_adult = False
    print("You are not an adult.")
else:
    print("You are an adult.")