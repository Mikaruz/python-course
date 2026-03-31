# Evaluar condiciones

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
#
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
#
# print(not True)
# print(not False)

age = 25
has_license = True
can_rent_car = age >= 21 and has_license
print("Can rent car:", can_rent_car)

is_student = False
has_discount = is_student or age < 18
print("Has discount:", has_discount)

is_admin = False

if not is_admin:
    print("Access denied: Admins only")