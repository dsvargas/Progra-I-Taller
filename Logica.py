__author__ = 'Dylana'
#Nombre: Dylana Sancho
#Fecha de entrega: 17-09-2014
#horas de trabajo:

#from Main import *



tipovariable = [{"int":"num"},{"float":"deci"},{"str":"letter"},{"True":"V"},{"False":"F"}]

Condicionales = [{"if":"si"},{"elif":"sifi"},{"else":"sino"}]

Bucles = [{"while":"mientras"},{"for":"hagase"}]

Funciones = [{"print":"imprimir"},{"def":"funka"},{"return":"retorne"},{"":""}]

sintaxis = [{":":";"},{"[":"("},{"]":")"},{"(":"{"},{")":"}"},{" ":"_"},{"    ":"//"}]


def reading(lineas):
    while True:
        line = input()
        if line == "listo":
            return
        lineas.append(line)

