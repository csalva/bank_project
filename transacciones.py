__author__ = 'cristina'


class Transaccion():
    def __init__(self, titular,nif,iban,saldo):
        self.nombreTitular=titular
        self.nif=nif
        self.iban=iban
        self.saldo=saldo

    def buscarCliente(self,identificacion):
        with open('cuentas.txt', mode='r', encoding='utf-8')as archivo:
            for i in archivo:
                nombreTitular,nif,numeroCuenta,saldoCuenta = i.split('-',4);
                if nombreTitular == nombreTitular and nif == nif:
                    print(nombreTitular,nif,numeroCuenta,saldoCuenta)
                else:
                    print("Error de identificacion")

    #def Ingresar(self):

    #def Retirar(self):

