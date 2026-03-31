name = input("Enter your name: ")
years_experience = int(input("Enter your years experience: "))
skills = input("Enter your skills (comma separated): ").lower().split(',')

if years_experience >= 3 and 'python' in [skill.strip() for skill in skills]:
    print(f"Congratulations {name}, you are eligible for the senior developer position!")
elif years_experience >= 1 and 'python' in [skill.strip() for skill in skills]:
    print(f"Congratulations {name}, you are eligible for the junior developer position!")
elif 'python' in [skill.strip() for skill in skills]:
    print(f"Congratulations {name}, you are eligible for the intern developer position!")
else:
    print(f"Sorry {name}, you are not eligible for any developer positions at this time.")