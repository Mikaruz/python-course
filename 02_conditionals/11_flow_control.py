age = int(input("What is your age?: "))

if age >= 18:
    print("You are old enough to go ahead")
    if age >= 65:
        print("You are eligible for a senior citizen discount.")
    else:
        print("You are not eligible for a senior citizen discount.")
else:
    print("You are not old enough to go ahead")
    if age < 13:
        print("You are a child.")
    else:
        print("You are a teenager.")
