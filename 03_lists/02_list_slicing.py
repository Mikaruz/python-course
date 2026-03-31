shopping_cart = ["apples", "bananas", "oranges", "grapes", "pears", "peaches"]

print(shopping_cart[3])

# [Inicio : Fin : Paso] | Crea una lista nueva a partir de una existente
print(shopping_cart[1:4])  # De la posición 1 a la 3 (el 4 no se incluye)
print(shopping_cart[:3])  # Desde el inicio hasta la posición 2
print(shopping_cart[2:])  # Desde la posición 2 hasta el final
print(shopping_cart[::2])  # Todos los elementos, pero de 2 en 2
print(shopping_cart[::-1])  # La lista al revés

new_cart = shopping_cart[:]
new_cart[0] = "banana"

print("Shopping Cart:", shopping_cart)
print("New Cart:", new_cart)
