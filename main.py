def calculadora_propina(total_factura, procentaje_propina):
    #Calcula el monto de la propina
    propina = total_factura * (procentaje_propina/100)
    return propina

def main():
    print("\n\t¡Bienvenido a la calculadora de Propinas!")
    
    try:
        total_factura = float(input("\nIngrese el monto de la factura: "))
        porcentaje_propina = float(input("Ingrese el porcentaje de la propina: "))

        propina = calculadora_propina(total_factura, porcentaje_propina)

        print(f"\nMonto de la propina: ${propina:.2f}")
        print(f"Monto total con propina: ${total_factura + propina:.2f}")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el monto total de la factura y el porcentaje de propina.")

if __name__ == "__main__":
    main()