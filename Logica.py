__author__ = 'Dylana'
# Nombre: Dylana Sancho
# Fecha de entrega: 17-09-2014
# horas de trabajo:


tipovariable = {"num":"int", "deci": "float", "letter": "str", "V": "True", "F": "False"}

Condicionales = {'si': 'if', "sifi": "elif", "sino": "else"}

Bucles = {"mientras": "while", "hagase": "for"}

Funciones = {"imprimir": "print", "funka": "def", "retorne": "return"}

sintaxis = {";": ":", "(": "[", ")": "]", "{": "(", "}": ")", "_": " ", "    ": "//"}


def writing(lineas): #escribe lineas
    while True:
        line = input()
        if line == "listo": # si encuentra " listo " se detiene la escritura
            return
        lineas.append(line)# las agraga a la lista lineas


def crear_archivo(): # crea un archivo
    archivo = open('archivo.txt', 'w')  # asi creamos un archivo
    archivo.close()


def escribe(lineas): # escribe las lineas que escribimos  al escojer "nuevo archivo"
    archivo = open('archivo.txt', 'a', 1)
    for i in range(len(lineas)): # recorre toda la lista
        for elemento in lineas[i]: # recorre la posicion i de la lista
            if elemento == ",":   # si encuentra una coma escribe
                archivo.write(":"+'\n') # todo lo que ya ha leido y hace un salto de linea
            else:
                archivo.write(elemento + " ") # escribe todo elemento
        archivo.write(" " + '\n')  # espacio y un salto de linea
    archivo.close()  # cierra el archivo


def leer_txten_lista(newLine): # lee las lineas de el archivo
    archivo=open('archivo.txt','r')  # abre el archivo y lo lee
    linea=archivo.readlines() # me guarda lo que lee en el archivo
    newLine.append(linea) # lo agrega a newlines
    print (linea)
    archivo.close()

#____________________________________________________________________________________

def separa(lineas):  # separa las lineas
    lineas_aux = [] 
    palabra = []
    for palabra in lineas: # recorre la lista " lineas "  donde escribimos el progama 
        palabra = palabra.split(" ")# cada que encuentre un espacio separa en palabras
        lineas_aux.extend(palabra)
    lineas[:] = lineas_aux[:]

def cambia(lineas):
    lineas_aux = []
    for i in range(len(lineas)):    #recorre las listas dentro de lineas
        temp = []
        for elemento in lineas[i]:  # agarra los elementos lista por lista
            if elemento in Condicionales:
                temp.append(Condicionales.get(elemento))
            elif elemento in Bucles:
                temp.append(Bucles.get(elemento))
            elif elemento in Funciones:
                temp.append(Funciones.get(elemento))
            elif elemento in sintaxis:
                temp.append(sintaxis.get(elemento))
            elif elemento in tipovariable:
                temp.append(tipovariable.get(elemento))
            else:
                temp.append(elemento)
        lineas_aux.append(temp)

    lineas[:] = lineas_aux[:]
'''
def cambia(lineas):
    listaAux = []
    for i in lineas:
        if i in Condicionales:
            for j in Condicionales[i]:
                listaAux.append(Condicionales[j])
        else:
            listaAux.append(i)
    lineas[:] = listaAux[:]

def escribe(lineas):
    archivo = open('archivo.py', 'a', 1)
    for elemento in lineas:
        print(elemento)
        if elemento != "":
            archivo.write(elemento+" ")
        else:
            archivo.write(" "+'\n')

    archivo.close()

    #return lineas
'''




