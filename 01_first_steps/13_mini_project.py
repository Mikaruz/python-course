name = input("Enter your name: ")
email = input("Enter your email: ")
age = input("Enter your age: ")
password = input("Enter your password: ")

card = f"""
    Name: {name}
    Email: {email}
    Age in 2050: {int(age) + 25} years old
    Password: {'*' * len(password)}
"""

print(card)