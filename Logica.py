__author__ = 'Dylana'
# Nombre: Dylana Sancho
# Fecha de entrega: 17-09-2014
# horas de trabajo:


tipovariable = {"int": "num", "float": "deci", "str": "letter", "True": "V", "False": "F"}

Condicionales = {'si': 'if', "sifi": "elif", "sino": "else"}
Bucles = {"while": "mientras", "for": "hagase"}
Funciones = {"print": "imprimir", "def": "funka", "return": "retorne"}
sintaxis = {":": ";", "[": "(", "]": ")", "(": "{", ")": "}", " ": "_", "    ": "//"}


def writing(lineas): #escribe lineas
    while True:
        line = input()
        if line == "listo": # si encuentra " listo " se detiene la escritura
            return
        lineas.append(line)# las agraga a la lista lineas

def separa(lineas):  # separa las lineas
    lineas_aux = [] 
    palabra = []
    for palabra in lineas: # recorre la lista " lineas "  donde escribimos el progama 
        palabra = palabra.split(" ")# cada que encuentre un espacio separa en palabras
        lineas_aux.extend(palabra)
    lineas[:] = lineas_aux[:]

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

def crear_archivo():
    archivo = open('archivo.py', 'w')  # asi creamos un archivo .py
    archivo.close()


