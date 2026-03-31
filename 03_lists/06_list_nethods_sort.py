letters = ['m', 'a', 'b', 'c', 'd', 'w', 'z', 'e']
print(letters)

# sort()
letters.sort()

# sorted() crea un nuevo arrays
new_letters = sorted(letters)

print(new_letters)

new_letters = letters[:]  # List Slicing

new = letters.copy()
print(new)
print(new_letters)

# Reverse
letters.reverse()
print(letters)
