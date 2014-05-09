__author__ = 'cristina'


class Transaccion():
    def __init__(self, identificacion,dni,iban,saldo):
        self.nombreTitular=identificacion
        self.nif=dni
        self.numeroCuenta=iban
        self.saldoCuenta=saldo

    def buscarCliente(self,identificacion):
        with open('cuentas.txt', mode='r', encoding='utf-8')as archivo:
            for i in archivo:
                nombreTitular,nif,numeroCuenta,saldoCuenta = i.split('-',4);



    #def Ingresar(self):

    #def Retirar(self):
