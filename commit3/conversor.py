# Conversor con Bucle - Commit 3
print("=== CONVERSOR INTERACTIVO ===")
while True:
    valor = float(input("\nIngrese valor (0 para salir): "))
    if valor == 0:
        print("¡Hasta luego!")
        break
    
    unidad_origen = input("Unidad (C/F): ").upper()
    if unidad_origen == "C":
        print(f"{valor}°C = {(valor * 9/5) + 32}°F")
    elif unidad_origen == "F":
        print(f"{valor}°F = {(valor - 32) * 5/9}°C")
    else:
        print("Unidad no soportada.")