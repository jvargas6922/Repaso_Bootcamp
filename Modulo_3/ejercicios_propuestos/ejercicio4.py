print("=== PAGO DE PERMISO DE CIRCULACION ===")

# Tipo de vehiculo
while True:
    print("\nTipos de vehiculo:")
    print("1. Automovil - $80.00")
    print("2. Motocicleta - $40.00")
    print("3. Camioneta - $100.00")
    opcion_vehiculo = input("Selecciona el tipo de vehiculo (1-3): ")

    if opcion_vehiculo == "1":
        tipo_vehiculo = "Automovil"
        costo_base = 80.00
        break
    elif opcion_vehiculo == "2":
        tipo_vehiculo = "Motocicleta"
        costo_base = 40.00
        break
    elif opcion_vehiculo == "3":
        tipo_vehiculo = "Camioneta"
        costo_base = 100.00
        break
    else:
        print("Opcion invalida. Intenta nuevamente.")

# Fecha de vencimiento
while True:
    fecha_vencimiento = input("\nIngresa la fecha de vencimiento (DD/MM/AAAA): ").strip()
    if fecha_vencimiento == "":
        print("La fecha no puede estar vacia.")
    else:
        break

# Metodo de pago
while True:
    print("\nMetodos de pago:")
    print("1. Tarjeta de credito")
    print("2. Transferencia bancaria")
    print("3. Efectivo")
    opcion_pago = input("Selecciona el metodo de pago (1-3): ")

    if opcion_pago == "1":
        metodo_pago = "Tarjeta de credito"
        break
    elif opcion_pago == "2":
        metodo_pago = "Transferencia bancaria"
        break
    elif opcion_pago == "3":
        metodo_pago = "Efectivo"
        break
    else:
        print("Opcion invalida. Intenta nuevamente.")

# Servicios adicionales
while True:
    recordatorio = input("\nDeseas agregar recordatorio de vencimiento? (s/n): ").lower()
    if recordatorio == "s":
        costo_recordatorio = 2.00
        detalle_recordatorio = "Si"
        break
    elif recordatorio == "n":
        costo_recordatorio = 0.00
        detalle_recordatorio = "No"
        break
    else:
        print("Respuesta invalida. Escribe 's' o 'n'.")

while True:
    descuento = input("Deseas aplicar descuento por pago anticipado? (s/n): ").lower()
    if descuento == "s":
        descuento_aplicado = costo_base * 0.10
        detalle_descuento = "Si"
        break
    elif descuento == "n":
        descuento_aplicado = 0.00
        detalle_descuento = "No"
        break
    else:
        print("Respuesta invalida. Escribe 's' o 'n'.")

# Calculo total
total = costo_base + costo_recordatorio - descuento_aplicado

# Resumen final
print("\n=== RESUMEN DEL PAGO ===")
print("Tipo de vehiculo:", tipo_vehiculo, "- $", format(costo_base, ".2f"))
print("Fecha de vencimiento:", fecha_vencimiento)
print("Metodo de pago:", metodo_pago)
print("Recordatorio de vencimiento:", detalle_recordatorio, "- $", format(costo_recordatorio, ".2f"))
print("Descuento por pago anticipado:", detalle_descuento, "- $", format(descuento_aplicado, ".2f"))
print("Total a pagar: $", format(total, ".2f"))
print("Pago procesado correctamente.")