#EJERCICIO_8_2

def calcular_intereses(capital,tasa_interes,tiempo_meses):
    intereses=(capital*tasa_interes/100)*tiempo_meses
    return intereses

def CapitalFinal(capital,intereses):
    capital_final=capital+intereses 
    return capital_final

def main():
    capital=float(input("Ingrese el capital invertido en €: "))
    tasa_interes=float(input("Ingrese el tasa de interés (en porcentaje):"))
    tiempo_meses=int(input("Ingrese los meses sobre los cuales se calcularía: "))
    intereses=calcular_intereses(capital,tasa_interes,tiempo_meses)
    capital_final=CapitalFinal(capital,intereses)
    print(f"los intereses generados son {intereses} €.")
    print(f"el capiatal final es {capital_final} €.")    
main()