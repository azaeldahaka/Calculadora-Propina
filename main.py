#Func. calculadora de propina
def calculadora_propina(total_factura, procentaje_propina):
    #Calcula el monto de la propina
    propina = total_factura * (procentaje_propina/100)
    return propina

#Func. principal
def main():
    print("\n\t¡Bienvenido a la calculadora de Propinas!")
    
    try:
        #Pedimos datos sobre los montos
        total_factura = float(input("\nIngrese el monto de la factura: "))
        porcentaje_propina = float(input("Ingrese el porcentaje de la propina: "))

        #Llamamos a la func. calculadora_propina
        propina = calculadora_propina(total_factura, porcentaje_propina)

        #Mostramos los resultados calculados.
        print(f"\n\tMonto de la propina: ${propina:.2f}")
        print(f"\tMonto total con propina: ${total_factura + propina:.2f}")
    
    #Manejamos excepciones
    except ValueError:
        print("Error: Por favor ingrese un número válido para el monto total de la factura y el porcentaje de propina.")

if __name__ == "__main__":
    main()