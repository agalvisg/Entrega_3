def area_triangulo(lado,altura):
    """calcula el área de un triángulo según un lado y la altura relativa a ese lado
    
    Args:
        Lado(float): Medida de uno de los lados. 
                    En caso de ser un triángulo rectángulo usar uno de los catetos.
        Altura(float): Medida de la altura relativa a ese lado.
                    En caso de ser un triángulo rectángulo usar el otro cateto.  
    
    Returns: 
        Float: Área del triángulo.    
    """
    area=(lado*altura)/2
    return area

def main():
    
    lado=float(input("Ingrese la medida de un lado del triángulo: "))
    altura=float(input("Ingrese la medida de la altura del triángulo relativa al lado: "))
    
    area=area_triangulo(lado,altura)
    
    print(f"El área del triángulo es: {area}")
    
if __name__== "__main__":
    main()