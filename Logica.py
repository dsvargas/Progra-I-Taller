__author__ = 'Dylana'
# Nombre: Dylana Sancho
# Fecha de entrega: 17-09-2014
# horas de trabajo:


tipovariable = {"int": "num", "float": "deci", "str": "letter", "True": "V", "False": "F"}

Condicionales = {'if': 'si', "elif": "sifi", "else": "sino"}

Bucles = {"while": "mientras", "for": "hagase"}

Funciones = {"print": "imprimir", "def": "funka", "return": "retorne"}

sintaxis = {":": ";", "[": "(", "]": ")", "(": "{", ")": "}", " ": "_", "    ": "//"}


def reading(lineas):
    while True:
        line = input()
        if line == "listo":
            return
        lineas.append(line)


def revisa(lineas):
    lineas_aux = []
    for palabra in lineas:
        palabras = []
        palabras = palabra.split(" ")
        lineas_aux.extend(palabras)
    lineas[:] = lineas_aux[:]
    lineas_aux = []


def escribe(lineas):
    archivo = open('archivo.py', 'a',1)
    for elemento in lineas:
        print(elemento)
        if elemento!= ";":
            archivo.write(elemento+" ")
        else:
            archivo.write(":"+'\n')

    archivo.close()

    #return lineas

def crear_archivo():
    archivo = open('archivo.py', 'w')  # asi creamos un archivo .py
    archivo.close()

'''

def identificar_estud(Condicionales):
    carnet = input("Digite el carnet del estudiante: ")
    if carnet in Condicionales.keys(): # si carnet es en las llaves de el diccionario de estudiantes
        print("El estudiante al cual le pertenece ese carnet es ", Condicionales[carnet])
    else:
        print("Estudiante no encontrado")
'''






