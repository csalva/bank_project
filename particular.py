__author__ = 'cristina'

from random import randrange

class Particular():
    def __init__(self, nombreParticular,apellidosParticular,nif):
        self.nombreParticular = nombreParticular
        self.apellidosParticular = apellidosParticular
        self.nif = nif

    def getNombreParticular(self):
        return self.nombreParticular

    def getApellidosParticular(self):
        return self.apellidosParticular

    def getNif(self):
        return self.nif

    def crearCuenta(self):
        iban = str(randrange(1000,9999))
        iban += " "+str(randrange(1000,9999))
        iban += " "+str(randrange(10,99))
        iban += " "+str(randrange(1000000000,9999999999))

        registro = (self.nombreParticular+"-"+self.apellidosParticular+"-"+self.nif+"-"+iban+"-"+0,00)
        with open('cuentas.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(registro)
            print(registro)
