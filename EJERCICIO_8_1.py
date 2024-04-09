#EJERCICIO 8 apartado 1.

def precio_sin_impuestos():
    
    #Se ingresa el precio del producto sin impuestos
    
    precio=float(input("Ingrese el precio del producto (euros): "))
    return precio

class TipoProducto():
    
    #clase para definir el tipo de producto
    
    def __init__(self,tipo):
        self.tipo = tipo
        
    def get_tipo(self):
        return self.tipo
    
class Impuestos(TipoProducto):
    
    # Clase para calcular los impuestos sobre el precio según el tipo de producto.
    
    def __init__(self,tipo,IVA,especial):
        
        super().__init__(tipo)
        self.IVA=IVA
        self.especial=especial

    def calcular_impuestos (self,precio_sin_impuestos):
        
        # Función de cálculo
        
        if self.tipo == "ordinario":
            
            impuestos=precio_sin_impuestos*(self.IVA/100)
            return impuestos
        
        else:
        
            impuestos=precio_sin_impuestos*(self.especial/100)+precio_sin_impuestos*(self.IVA/100)
            return impuestos   



def PrecioFinal(precio_sin_impuestos,impuestos_calculados):
    
    # Resultado precio final
    
    precio_final=precio_sin_impuestos+impuestos_calculados
    return precio_final

def main():
    # Ingresar los datos
    tipo=input("¿De qué tipo de producto desea calcular el precio?(ordinario, alcohol, hidrocarburos, tabaco) ")
    precio=precio_sin_impuestos()
    tipo_producto=TipoProducto(tipo)
    
    # Condicionales para relacionar el tipo de producto con los impuestos que se van a aplicar.
    # A parte del IVA hay productos a los que se suman impuestos especiales.
    # Si no es ordinario, alcohol, tabaco o hidrocarburo no será válido.
    
    if tipo in ["ordinario"]:
        IVA=21
        imp=Impuestos(tipo,IVA,0)
    elif tipo in ["alcohol","hidrocarburos","tabaco"]:
        IVA=21
        especial=float(input("Ingrese el porcentaje de impuestos especiales correspodiente al producto:"))
        imp=Impuestos(tipo,IVA,especial)
    else:
        print("tipo de producto no válido.")
        return tipo
        
    impuestos_calculados=imp.calcular_impuestos(precio)
    
    # Calculo del precio final
    
    precio_final=PrecioFinal(precio,impuestos_calculados)
    
    # Imprimir los resultados
    print(f"Los impuestos para el producto {tipo} son : {impuestos_calculados} €")
    print(f"el precio final a pagar del producto será de {precio_final} € con IVA incluido e impuestos especiales.")
    
if  __name__=="__main__":
    main()
    