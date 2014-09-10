__author__ = 'Dylana'
# Nombre: Dylana Sancho
#Fecha de entrega: 17-09-2014
#horas de trabajo:

from Logica import *

lineas = []


def main():
    print("1.Nuevo archivo")
    print("2.Compilar")
    try:
        qs = int(input("Escoja la opcion que desee."))
        if qs == 1:
            print("Nuevo archivo")
            reading(lineas)
        elif qs == 2:
            print("Compilar")
        else:
            print("cosita")
            main()
    except:
        print("cosita")
        main()



def revisa(lineas):
    lineasAux = []
    for palabra in lineas:
        palabraS=[]
        palabraS = palabra.split(" ")
        lineasAux.extend(palabraS)
    lineas[:] = lineasAux[:]
    return  lineas




main()
print(lineas)
print(revisa(lineas),"cosita")