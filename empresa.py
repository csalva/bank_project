__author__ = 'cristina'

from random import randrange

class Empresa():
    def __init__(self, razonSocial,cif):
        self.razonSocial = razonSocial
        self.cif = cif

    def getRazonSocial(self):
        return self.razonSocial

    def getCif(self):
        return self.cif

    def crearCuenta(self):
        iban = str(randrange(1000,9999))
        iban += " "+str(randrange(1000,9999))
        iban += " "+str(randrange(10,99))
        iban += " "+str(randrange(1000000000,9999999999))

        registro = (self.razonSocial+"-"+self.cif+"-"+iban+"-"+0,00)

        with open('cuentas.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(registro)
            print(registro)
