__author__ = 'Dylana'
# Nombre: Dylana Sancho
#Fecha de entrega: 17-09-2014
#horas de trabajo:

from Logica import *

lineas = [] # las lineas que escribimos en el txt
newLine = [] # las lineas que escribimos en el py

def main():
    print("1.Nuevo archivo")
    print("2.Compilar")
    try:
        qs = int(input("Escoja la opcion que desee."))
        if qs == 1:
            print("Nuevo archivo")
            writing(lineas)
            print(lineas)
            crear_archivo()
            escribe(lineas)
            leer_txten_lista(newLine)
        elif qs == 2:
            print("Compilar")
        else:
            print("cosita")
            main()
    except:
        print("se enciclo")
        main()





main()
print(newLine,"an blublublu")