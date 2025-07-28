# Conversor Básico - Commit 1
print("=== CONVERSOR SIMPLE ===")
valor = float(input("Ingrese valor: "))
unidad_origen = input("Unidad origen (C/F/USD/CLP/m/km): ").upper()
unidad_destino = input("Unidad destino (C/F/USD/CLP/m/km): ").upper()
print(f"\nConvertir {valor} {unidad_origen} a {unidad_destino}...")