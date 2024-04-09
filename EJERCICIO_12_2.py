# EJERCICIO_12_2

class CuentaDepositoConDescubierto:
    
    def __init__(self,saldo_inicial,limite_descubierto=0):
        self.saldo=saldo_inicial
        self.limite_descubierto=limite_descubierto
        
    def depositar(self, monto):
        self.saldo+=monto
        
    def retirar(self, monto):
        if self.saldo - monto>= -self.limite_descubierto:
            self.saldo -= monto
            return True
        else:
            print("Fondos insuficientes")
            return False
        
    def consultar_saldo(self):
        return self.saldo
    
    
def main():
    cuenta=CuentaDepositoConDescubierto(1000,200)
    print("saldo inicial:", cuenta.consultar_saldo())
    cuenta.depositar(500)
    print("Saldo después del depósito: ", cuenta.consultar_saldo())
    cuenta.retirar(1600) 
    print("saldo después del retiro:", cuenta.consultar_saldo())
    

if __name__=="__main__":
    main()
            