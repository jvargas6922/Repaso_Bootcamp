print("=== SISTEMA DE PEDIDO MCDONALD'S ===")

MENSAJE_OPCION_INVALIDA = "Opcion invalida. Intenta nuevamente."

# Seleccion de comida
while True:
    print("\nMenu de comida:")
    print("1. Hamburguesa - $5.00")
    print("2. Nuggets - $4.50")
    print("3. McWrap - $6.00")
    opcion_comida = input("Selecciona una comida (1-3): ")

    if opcion_comida == "1":
        comida = "Hamburguesa"
        precio_comida = 5.00
        break
    elif opcion_comida == "2":
        comida = "Nuggets"
        precio_comida = 4.50
        break
    elif opcion_comida == "3":
        comida = "McWrap"
        precio_comida = 6.00
        break
    else:
        print(MENSAJE_OPCION_INVALIDA)

# Seleccion de bebida
while True:
    print("\nMenu de bebida:")
    print("1. Coca-Cola - $2.00")
    print("2. Jugo - $2.50")
    print("3. Agua - $1.50")
    opcion_bebida = input("Selecciona una bebida (1-3): ")

    if opcion_bebida == "1":
        bebida = "Coca-Cola"
        precio_bebida = 2.00
        break
    elif opcion_bebida == "2":
        bebida = "Jugo"
        precio_bebida = 2.50
        break
    elif opcion_bebida == "3":
        bebida = "Agua"
        precio_bebida = 1.50
        break
    else:
        print(MENSAJE_OPCION_INVALIDA)

# Seleccion de postre
while True:
    print("\nMenu de postre:")
    print("1. Helado - $2.00")
    print("2. Pie de manzana - $2.20")
    print("3. Galleta - $1.80")
    opcion_postre = input("Selecciona un postre (1-3): ")

    if opcion_postre == "1":
        postre = "Helado"
        precio_postre = 2.00
        break
    elif opcion_postre == "2":
        postre = "Pie de manzana"
        precio_postre = 2.20
        break
    elif opcion_postre == "3":
        postre = "Galleta"
        precio_postre = 1.80
        break
    else:
        print(MENSAJE_OPCION_INVALIDA)

# Opcion de agrandar pedido
while True:
    agrandar = input("\nDeseas agrandar tu pedido? (s/n): ").lower()

    if agrandar == "s":
        extra_agrandar = 1.50
        detalle_agrandar = "Si"
        break
    elif agrandar == "n":
        extra_agrandar = 0.00
        detalle_agrandar = "No"
        break
    else:
        print("Respuesta invalida. Escribe 's' o 'n'.")

# Calculo total
total = precio_comida + precio_bebida + precio_postre + extra_agrandar

# Resumen
print("\n=== RESUMEN DEL PEDIDO ===")
print("Comida:", comida, "- $", format(precio_comida, ".2f"))
print("Bebida:", bebida, "- $", format(precio_bebida, ".2f"))
print("Postre:", postre, "- $", format(precio_postre, ".2f"))
print("Agrandar pedido:", detalle_agrandar, "- $", format(extra_agrandar, ".2f"))
print("Total a pagar: $", format(total, ".2f"))