__author__ = 'cristina'

from random import randrange

class Particular():
    def __init__(self, nombreParticular,nif):
        self.nombreParticular = nombreParticular
        self.nif = nif

    def getNombreParticular(self):
        return self.nombreParticular

    def getNif(self):
        return self.nif

    def crearCuenta(self):
        iban = str(randrange(1000,9999))
        iban += " "+str(randrange(1000,9999))
        iban += " "+str(randrange(10,99))
        iban += " "+str(randrange(1000000000,9999999999))

        registro = (self.nombreParticular+"-"+self.nif+"-"+iban+"-"+"0,00"+"\n")
        with open('cuentas.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(registro)
            print(registro)
