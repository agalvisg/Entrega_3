#EJERCICIO_12

class cuenta_deposito:
    def __init__(self,saldo_inicial):
        self.saldo=saldo_inicial
        
    def depositar(self, monto):
        self.saldo+=monto
        
    def retirar(self,monto):
        if self.saldo - monto>=0:
            self.saldo-=monto
            return True
        else:
            print("saldo insuficiente")
            return False
        
    def consultar_saldo(self):
        return self.saldo
    
def main():
    
    cuenta=cuenta_deposito(1000) #crear cuenta con saldo inicial de 1000
    
    print("Saldo inicial:", cuenta.consultar_saldo())
    cuenta.depositar(500)
    print("Saldo después del depósito:", cuenta.consultar_saldo())
    cuenta.retirar(200)
    print("Saldo después del retiro:", cuenta.consultar_saldo())
    
if __name__==  "__main__":
    main()