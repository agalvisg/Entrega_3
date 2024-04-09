#EJERCICIO_9_1

def MediaAritmetica(n1,n2,n3):
    
    """El usuario ingresa los 3 números como float.
    Args: n1, n2, n3       

    Devuelve:
        Media aritmética de los 3 números.
    """
    media=(n1+n2+n3)/3
    return media

def MediaPonderada(numeros,ponderaciones):
    """Calcula la media ponderada de una lista de números con sus correspondientes ponderaciones.
    

    Args:
        numeros (list): una lista de números
        ponderaciones (list): lista de ponderaciones para los números.
    
    Returns:
        float: media ponderada de los números.
    
    """ 
    total=sum(num*ponder for num, ponder in zip(numeros,ponderaciones))
    suma_ponderaciones=sum(ponderaciones)
    media= total/suma_ponderaciones
    return media

def main():
    
    #el usuario elige si quiere hacer una media ponderada o aritmetica
    eleccion=(input("¿Desea hacer una media ponderada o aritmética? (aritmetica/ponderada) "))
    
    if eleccion == "aritmetica": 
    # Media Aritméica
        n1=float(input("Ingrese el primer número: "))
        n2=float(input("Ingrese el segundo número: "))
        n3=float(input("Ingrese el tercer número: "))
            
        media_aritmetica=MediaAritmetica(n1,n2,n3)
    
        print(f"La media resultante sería: {media_aritmetica}")
    elif eleccion=="ponderada":
        numeros=[]
        ponderaciones=[]
        for i in range(3):
            numero=float(input(f"ingrese el número {i+1}: "))
            numeros.append(numero)
            ponderacion=float(input(f"ingrese la ponderación para el número {i+1} (en porcentaje): "))
            ponderaciones.append(ponderacion)
        
        media_ponderada=MediaPonderada(numeros,ponderaciones)
        print(f"la media ponderada es: {media_ponderada}")
        
    else:
        print("No has esccogido una opción válida.")
        return eleccion


if __name__=="__main__":
    main()
     