# Conversor Modular - Commit 4
def convertir_temperatura(valor, origen, destino):
    if origen == "C" and destino == "F":
        return (valor * 9/5) + 32
    elif origen == "F" and destino == "C":
        return (valor - 32) * 5/9
    return None

def convertir_moneda(valor, origen, destino):
    tasas = {"USD": 1, "CLP": 950}  # 1 USD = 950 CLP
    if origen in tasas and destino in tasas:
        return valor * tasas[destino] / tasas[origen]
    return None

print("=== CONVERSOR AVANZADO ===")
while True:
    valor = float(input("\nIngrese valor (0 para salir): "))
    if valor == 0:
        break
    
    print("Opciones:")
    print("1. Temperatura (°C <-> °F)")
    print("2. Moneda (USD <-> CLP)")
    opcion = input("Elija tipo de conversión (1/2): ")

    if opcion == "1":
        origen = input("Unidad origen (C/F): ").upper()
        destino = "F" if origen == "C" else "C"
        resultado = convertir_temperatura(valor, origen, destino)
        if resultado:
            print(f"{valor} {origen} = {resultado:.2f} {destino}")
        else:
            print("Error en unidades.")
    elif opcion == "2":
        origen = input("Unidad origen (USD/CLP): ").upper()
        destino = "CLP" if origen == "USD" else "USD"
        resultado = convertir_moneda(valor, origen, destino)
        if resultado:
            print(f"{valor} {origen} = {resultado:.2f} {destino}")
        else:
            print("Error en unidades.")
    else:
        print("Opción no válida.")