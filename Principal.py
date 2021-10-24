#Aqui se define la interfaz por consola con el jugador
from ClassJuego import *
import json
print("=================================================================")
print("          BIENVENIDO A ¿QUIÉN QUIERE SER MILLONARIO?      ")
print("=================================================================")

while True:
    jugador = input("Por favor ingrese su nombre: ")
    if not jugador.isalpha():
        print("Nombre de usuario no valido")
    else:
        break
juego=Juego(jugador,True)
ronda = 4
i = 0
datos = {}
datos['Jugadores'] = []
while i <= ronda:
    cat = juego.seleccionarCategoria(i)
    juego.seleccionarPregunta(cat)
    juego.respuesta()
    juego.validarRespuesta(cat)
    if juego.status == False:
        print(f"{jugador} su premio acumulado es de ", 0, " millon(es) de pesos, dado que perdio el juego\n")
        break
    juego.premio(i,ronda)
    if juego.status == False:
        print(f"{jugador} su premio acumulado es de  ", juego.acumPremio(i+1,ronda), "millon(es) de pesos")
        break
    if i == ronda:
        if juego.status == False:
            print(f"{jugador} su premio acumulado es de  ", juego.acumPremio(i,ronda), "millon(es) de pesos")
        else:
            print("\n==============FELICIDADES UD GANO EL JUEGO==================")
            print(f"{jugador} su premio acumulado es de  ", juego.acumPremio(i,ronda), "millon(es) de pesos")
    i += 1
datos['Jugadores'].append(juego.datos(i,ronda))


# escribir los datos en  un archivo json
with open('datos.json', 'a') as f:
    json.dump(datos,f)  
while True:
    consulta= int(input("¿Si desea consultar sus datos digite 1  ó  2 para salir? \n"))
    if consulta==1 or consulta==2:
        break
    else:
        print("Opcion no validad, ingrese 1 ó 2 por favor")
    
if consulta==1:
    print("======DATOS PERSONALES=======")
    for p in datos["Jugadores"]:
        print('Nombre:%s' % p['user'])
        print('Premio:%i'% p['premio'],"millon(nes) de pesos")
else:
    print("Gracias por jugar")

