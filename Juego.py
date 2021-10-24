from Preguntas import *
import random
import json

# Se construye la clase Juego con sus respectivos métodos y funciones
status = True
class Juego:

    def __init__(self, user):
        self.user = user

    #Esta funncion retorna una Pregunta aleatoria correspondiente a su categoria
    def seleccionarPregunta(self, cat):

        self.cat = cat
        global p
        p = random.choice(list(self.cat.keys()))
        print("\n", p, "\n")
        global opcion
        opcion = ["A", "B", "C", "D"]
        for i in range(len(cat[p])-1):
            print(opcion[i] + ".", cat[p][i],   end="\t")
        print('\n')
    #Esta funcion selecciona la caegoria
    def seleccionarCategoria(self, i):
        x = i+1
        if x == 1:
            print(f"\n*** RONDA {x}: {user} vamos por {x} millon(nes) de pesos***")
        else:
            y=(i+2)*2
            print(f"\n*** RONDA {i+1}: {user} vamos por {y} millon(nes) de pesos***")
        categorias = [Cat1, Cat2, Cat3, Cat4, Cat5]
        cat = categorias[i]
        i += 1
        return cat
    #Esta funcion recibe la respuesta y solicita confirmación
    def respuesta(self):
        global r
        r = input("Seleccione su respuesta: ").upper()
        while True:
            if (r != "A") and (r != "B") and (r != "C") and (r != "D"):
                r = input("Error al seleccionar respuesta: digite A, B, C o D: ").upper()
            else:
                break
        a=int(input("\n¿Ultima Palabra? \n Digite 1.Para continuar 2.Para cambiar su respuesta: "))
        if a == 2:
            while True:
                r = input("Cambie su respuesta seleccionada: digite A, B, C o D: ").upper()
                if (r != "A") and (r != "B") and (r != "C") and (r != "D"):
                    r = input("Error al seleccionar respuesta: digite A, B, C o D: ").upper()
                else:
                    break
        return r

    #Esta funcion valida si la respuesta ingresada corresponde a la respuesta correcta
    def validarRespuesta(self):
        global status
        for i in range(len(opcion)):
            if r == opcion[i]:
                x = i
        if cat[p][x] == cat[p][-1]:
            print("\n¡¡¡¡SU RESPUESTA ES CORRECTA!!!!")
        else:
            print("\n=====LA RESPUESTA NO ES CORRECTA===== \nUsted ha perdido :(\n")
            status = False
        return status
    #Esta funcion define el premio de cada ronda y la continuidad del mismo.
    def premio(self, i):
        global status
        if i == ronda:
            print("El Juego ha finalizado")
        else:
            c = int(input("\n==¿Desea usted continuar Jugando?== \n1.Si  2.No: "))
            while True:
                if (c == 1) or (c == 2):
                    break

                else:
                    c = int(input("Respuesta no valida: Por favor escriba 1 o 2: "))
            if c == 1:
                status = True
            else:
                status = False
        return status
    #Esta fuincion determina el premio acumulado del jugador
    def acumPremio(self, i):
        y = (i+2)*i
        if i == 0:
            return y*0
        elif i == 1:
            y = 1
        elif i == ronda:
            y = y
        else:
            y = y-2
        return y
    
    #Esta fuincion Captura los datos del Jugador
    def datos(self,i):
        datos = {}
        datos["user"]=self.user
        datos["premio"]=self.acumPremio(i+1)
        return datos


