#EJERCICIO 8

def precio_sin_impuestos():
    precio=float(input("Ingrese el precio del producto (euros): "))
    return precio

class TipoProducto():
    
    def __init__(self,tipo):
        self.tipo = tipo
        
    def get_tipo(self):
        return self.tipo
    
class Impuestos(TipoProducto):
    
    def __init__(self,tipo,IVA,especial) :
        super().__init__(tipo)
        self.IVA=IVA
        self.especial=especial

    def calcular_impuestos (self,precio_sin_impuestos):
        if self.tipo == "ordinario":
            impuestos=precio_sin_impuestos*(self.IVA/100)
            return impuestos
        else:
            impuestos=[precio_sin_impuestos*(self.especial/100)+precio_sin_impuestos*(self.IVA/100)]
            return impuestos   
    

def main():
    tipo=input("¿De qué tipo de producto desea calcular el precio?(ordinario, alcohol, hidrocarburos, tabaco)")
    precio=precio_sin_impuestos()
    tipo_producto=TipoProducto(tipo)
    
    if tipo in ["ordinario"]:
        IVA=21
        imp=Impuestos(tipo,IVA,0)
    elif tipo==["alcohol","hidrocarburos","tabaco"]:
        IVA=21
        especial=float(input("Ingrese el porcentaje de IVA correspodiente al producto:"))
        imp=Impuestos(tipo,IVA,especial)
    else:
        print("tipo de producto no válido.")
        return
    impuestos_calculados=imp.calcular_impuestos(precio)
    print(f"Los impuestos para el producto {tipo} son : {impuestos_calculados} €")
    
    
if  __name__=="__main__":
    main()
    