__author__ = 'cristina'

from empresa import Empresa
from particular import Particular
from transacciones import Transaccion

def menu():
    print("Bank Project")
    print("Es usted cliente? (Si/No)")


def subMenu():
    print("Desea registrarse? (Si/No)")

menu()
cliente = str(input())


iban = ''
saldo = 0

if cliente.upper() == "SI":
    print("Introduce el nombre y apellidos o razon social")
    titular = str(input())
    print("Introduzca el nif o cif")
    nif=str(input())
    print("1. Consultar saldo")
    Transaccion.buscarCliente(titular, nif)
    transaccio = Transaccion(titular,nif,iban,saldo)


    print("2. Transferencia")

elif cliente.upper() == "NO":
    subMenu()
    altaCliente = str(input())
    if altaCliente.upper() == "SI":
        print("Bienvenido")
        print("1. Cuenta para empresas: ")
        print("2. Cuenta para particulares: ")
        tipoCuenta = int(input())
        if tipoCuenta == 1:
            print("Introduce Razon Social")
            nombreEmpresa = str(input())
            print("Introduce el CIF")
            cif = str(input())
            empresa = Empresa(nombreEmpresa,cif)
            empresa.crearCuenta()

        if tipoCuenta == 2:
            print("Introduce Nombre y Apellidos")
            nombreParticular = str(input())
            print("Introduce NIF/NIE")
            nif = str(input())
            particular = Particular(nombreParticular,nif)
            particular.crearCuenta()


    elif altaCliente.upper() == "NO":
        menu()
