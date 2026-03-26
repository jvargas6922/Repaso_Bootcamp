print("=== SISTEMA DE RESERVA DE RESTAURANTE ===")

# Fecha de reserva
while True:
    fecha = input("Ingresa la fecha de la reserva (DD/MM/AAAA): ").strip()
    if fecha == "":
        print("La fecha no puede estar vacia.")
    else:
        break

# Hora de reserva
while True:
    hora = input("Ingresa la hora de la reserva (HH:MM): ").strip()
    if hora == "":
        print("La hora no puede estar vacia.")
    else:
        break

# Numero de personas
while True:
    entrada_personas = input("Ingresa el numero de personas: ")

    if entrada_personas.isdigit():
        personas = int(entrada_personas)
        if personas > 0:
            break
        else:
            print("El numero de personas debe ser mayor que 0.")
    else:
        print("Debes ingresar un numero valido.")

# Solicitudes especiales
while True:
    mesa_ventana = input("Deseas mesa cerca de la ventana? (s/n): ").lower()
    if mesa_ventana == "s":
        detalle_mesa = "Si"
        break
    elif mesa_ventana == "n":
        detalle_mesa = "No"
        break
    else:
        print("Respuesta invalida. Escribe 's' o 'n'.")

while True:
    menu_vegetariano = input("Deseas menu vegetariano? (s/n): ").lower()
    if menu_vegetariano == "s":
        detalle_vegetariano = "Si"
        break
    elif menu_vegetariano == "n":
        detalle_vegetariano = "No"
        break
    else:
        print("Respuesta invalida. Escribe 's' o 'n'.")

# Verificacion basica de disponibilidad
if personas <= 6:
    disponibilidad = "Disponible"
elif personas <= 12:
    disponibilidad = "Disponible con previa confirmacion"
else:
    disponibilidad = "No disponible para ese numero de personas"

# Confirmacion
print("\n=== RESUMEN DE LA RESERVA ===")
print("Fecha:", fecha)
print("Hora:", hora)
print("Numero de personas:", personas)
print("Mesa cerca de la ventana:", detalle_mesa)
print("Menu vegetariano:", detalle_vegetariano)
print("Estado de disponibilidad:", disponibilidad)

if disponibilidad == "No disponible para ese numero de personas":
    print("La reserva no puede confirmarse automaticamente.")
else:
    print("Reserva registrada correctamente.")