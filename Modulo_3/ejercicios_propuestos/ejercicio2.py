print("=== SISTEMA DE ENVIO DE PAQUETES ===")

# Tipo de envio
while True:
    print("\nTipos de envio:")
    print("1. Estandar - $5.00")
    print("2. Express - $10.00")
    print("3. Prioritario - $15.00")
    opcion_envio = input("Selecciona el tipo de envio (1-3): ")

    if opcion_envio == "1":
        tipo_envio = "Estandar"
        costo_envio = 5.00
        break
    elif opcion_envio == "2":
        tipo_envio = "Express"
        costo_envio = 10.00
        break
    elif opcion_envio == "3":
        tipo_envio = "Prioritario"
        costo_envio = 15.00
        break
    else:
        print("Opcion invalida. Intenta nuevamente.")

# Direccion de destino
while True:
    direccion = input("\nIngresa la direccion de destino: ").strip()
    if direccion == "":
        print("La direccion no puede estar vacia.")
    else:
        break

# Peso del paquete
while True:
    entrada_peso = input("Ingresa el peso del paquete en kg: ")

    try:
        peso = float(entrada_peso)
        if peso <= 0:
            print("El peso debe ser mayor que 0.")
        else:
            break
    except ValueError:
        print("Debes ingresar un numero valido.")

# Costo por peso
if peso <= 1:
    costo_peso = 2.00
elif peso <= 5:
    costo_peso = 5.00
elif peso <= 10:
    costo_peso = 8.00
else:
    costo_peso = 12.00

# Servicios adicionales
while True:
    seguro = input("\nDeseas agregar seguro? (s/n): ").lower()
    if seguro == "s":
        costo_seguro = 3.00
        detalle_seguro = "Si"
        break
    elif seguro == "n":
        costo_seguro = 0.00
        detalle_seguro = "No"
        break
    else:
        print("Respuesta invalida. Escribe 's' o 'n'.")

while True:
    seguimiento = input("Deseas agregar seguimiento? (s/n): ").lower()
    if seguimiento == "s":
        costo_seguimiento = 1.50
        detalle_seguimiento = "Si"
        break
    elif seguimiento == "n":
        costo_seguimiento = 0.00
        detalle_seguimiento = "No"
        break
    else:
        print("Respuesta invalida. Escribe 's' o 'n'.")

# Calculo total
total = costo_envio + costo_peso + costo_seguro + costo_seguimiento

# Resumen final
print("\n=== RESUMEN DEL ENVIO ===")
print("Tipo de envio:", tipo_envio, "- $", format(costo_envio, ".2f"))
print("Direccion:", direccion)
print("Peso:", peso, "kg - $", format(costo_peso, ".2f"))
print("Seguro:", detalle_seguro, "- $", format(costo_seguro, ".2f"))
print("Seguimiento:", detalle_seguimiento, "- $", format(costo_seguimiento, ".2f"))
print("Total de envio: $", format(total, ".2f"))