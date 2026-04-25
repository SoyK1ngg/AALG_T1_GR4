import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setsGanados = 0

equipo1 = Equipo("Los Tigres")
equipo2 = Equipo("Las Aguilas")

def RegistraSet(ganador):
    termino = False
    if ganador == 1:
        equipo1.setsGanados = equipo1.setsGanados + 1
        if equipo1.setsGanados == 3:
            equipo1.partidosGanados = equipo1.partidosGanados + 1
            equipo2.partidosPerdidos = equipo2.partidosPerdidos + 1
            print("  >> " + equipo1.nombre + " gano el partido!")
            termino = True
    elif ganador == 2:
        equipo2.setsGanados = equipo2.setsGanados + 1
        if equipo2.setsGanados == 3:
            equipo2.partidosGanados = equipo2.partidosGanados + 1
            equipo1.partidosPerdidos = equipo1.partidosPerdidos + 1
            print("  >> " + equipo2.nombre + " gano el partido!")
            termino = True
    if termino == True:
        equipo1.setsGanados = 0
        equipo2.setsGanados = 0
    return termino

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    equipo1.setsGanados = 0
    equipo2.setsGanados = 0
    numSet = 1
    terminoPartido = False
    while terminoPartido == False:
        p1 = Puntos()
        p2 = Puntos()

        while (p1 < 25 and p2 < 25) or p1 == p2:
            p1 = p1 + PuntosExtras()
            p2 = p2 + PuntosExtras()

        if p1 > p2:
            print("  Set " + str(numSet) + ": " + equipo1.nombre + " " + str(p1) + " - " + str(p2) + " " + equipo2.nombre + " -> Gana " + equipo1.nombre)
            terminoPartido = RegistraSet(1)
        else:
            print("  Set " + str(numSet) + ": " + equipo1.nombre + " " + str(p1) + " - " + str(p2) + " " + equipo2.nombre + " -> Gana " + equipo2.nombre)
            terminoPartido = RegistraSet(2)

        numSet = numSet + 1

def ResultadoTorneo():
    print("\n===== RESULTADO DEL TORNEO =====")
    print(equipo1.nombre + ": Ganados = " + str(equipo1.partidosGanados) + " | Perdidos = " + str(equipo1.partidosPerdidos))
    print(equipo2.nombre + ": Ganados = " + str(equipo2.partidosGanados) + " | Perdidos = " + str(equipo2.partidosPerdidos))
    print("================================")

    if equipo1.partidosGanados > equipo2.partidosGanados:
        print(f"{equipo1.nombre} son los campeones")
    elif equipo2.partidosGanados > equipo1.partidosGanados:
        print(f"{equipo2.nombre} son los campeones")
    else:
        print("PARTIDO DE DESEMPATE")
        print("================================")
        JugarPartido()
        if equipo1.partidosGanados > equipo2.partidosGanados:
            print(f"{equipo1.nombre} son los campeones")
        elif equipo2.partidosGanados > equipo1.partidosGanados:
            print(f"{equipo2.nombre} son los campeones") 

n = int(input("¿Cuantos partidos se jugaran? "))
i = 1
while i <= n:
    print("\n-- PARTIDO " + str(i) + ": " + equipo1.nombre + " vs " + equipo2.nombre + " --")
    JugarPartido()
    i = i + 1

ResultadoTorneo()
