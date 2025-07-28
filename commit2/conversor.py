# Conversor con Condicionales - Commit 2
print("=== CONVERSOR DE TEMPERATURA ===")
valor = float(input("Ingrese valor: "))
unidad_origen = input("Unidad (C/F): ").upper()

if unidad_origen == "C":
    print(f"{valor}°C = {(valor * 9/5) + 32}°F")
elif unidad_origen == "F":
    print(f"{valor}°F = {(valor - 32) * 5/9}°C")
else:
    print("Unidad no soportada en este commit.")