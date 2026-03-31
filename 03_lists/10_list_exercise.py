print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = input("Elige una opción (1-6): ")

if option == "1":
    product = input("Ingresa el nombre del producto a agregar: ")
    shopping_cart.append(product)
    print(f"{product} ha sido agregado al carrito.")
elif option == "2":
    product = input("Ingresa el nombre del producto a eliminar: ")
    if product in shopping_cart:
        shopping_cart.remove(product)
        print(f"{product} ha sido eliminado del carrito.")
    else:
        print(f"{product} no se encuentra en el carrito.")
elif option == "3":
    sorted_cart = sorted(shopping_cart)
    print("Lista de productos ordenada:")
    for item in sorted_cart:
        print(item)
elif option == "4":
    product = input("Ingresa el nombre del producto a buscar: ")
    if product in shopping_cart:
        print(f"{product} se encuentra en el carrito.")
    else:
        print(f"{product} no se encuentra en el carrito.")
elif option == "5":
    count = len(shopping_cart)
    print(f"Hay {count} productos en el carrito.")
elif option == "6":
    shopping_cart.clear()
    print("El carrito ha sido vaciado.")
else:
    print("Opción no válida.")

print(shopping_cart)
