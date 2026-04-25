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
    if ganador == 1:
        ganadorEquipo = equipo1
        perdedorEquipo = equipo2
    else:
        ganadorEquipo = equipo2
        perdedorEquipo = equipo1
    ganadorEquipo.setsGanados = ganadorEquipo.setsGanados + 1
    if ganadorEquipo.setsGanados == 3:
        ganadorEquipo.partidosGanados = ganadorEquipo.partidosGanados + 1
        perdedorEquipo.partidosPerdidos = perdedorEquipo.partidosPerdidos + 1
        ganadorEquipo.setsGanados = 0   # <-- usa la variable, no equipo1/equipo2
        perdedorEquipo.setsGanados = 0  # <-- idem
        print("  >> " + ganadorEquipo.nombre + " gano el partido!")
        return True
    return False

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    equipo1.setsGanados = 0
    equipo2.setsGanados = 0
    numSet = 1
    terminoPartido = False
    while not terminoPartido:  # <-- mas pythónico que == False
        p1 = Puntos()
        p2 = Puntos()
        while (p1 < 25 and p2 < 25) or p1 == p2:
            p1 = p1 + PuntosExtras()
            p2 = p2 + PuntosExtras()
        if p1 > p2:
            ganador = 1
            nombreGanador = equipo1.nombre
        else:
            ganador = 2
            nombreGanador = equipo2.nombre
        print("  Set " + str(numSet) + ": " + equipo1.nombre + " " + str(p1) + " - " + str(p2) + " " + equipo2.nombre + " -> Gana " + nombreGanador)
        terminoPartido = RegistraSet(ganador)
        numSet = numSet + 1

def ResultadoTorneo():
    print("\n===== RESULTADO DEL TORNEO =====")
    print(equipo1.nombre + ": Ganados = " + str(equipo1.partidosGanados) + " | Perdidos = " + str(equipo1.partidosPerdidos))
    print(equipo2.nombre + ": Ganados = " + str(equipo2.partidosGanados) + " | Perdidos = " + str(equipo2.partidosPerdidos))
    print("================================")

n = int(input("¿Cuantos partidos se jugaran? "))
i = 1
while i <= n:
    print("\n-- PARTIDO " + str(i) + ": " + equipo1.nombre + " vs " + equipo2.nombre + " --")
    JugarPartido()
    i = i + 1

ResultadoTorneo()
