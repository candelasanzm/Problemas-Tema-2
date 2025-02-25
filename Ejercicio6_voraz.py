HORA_INICIO = 0
HORA_FIN = 1

def ordena_reservas(reservas : list[tuple[int, int]]) -> list[tuple[int, int]] :
    """ Ordena las reservas por hora de inicio de menor a mayor """
    inicio = lambda reserva: reserva[0] # defino la funcion lambda para obtener la hora de inicio de cada reserva
    return sorted(reservas, key = inicio)

def buscar_pista_libre(reservas : list[tuple[int, int]]) -> list[tuple[int, int]]:
    """ Busca una pista libre, ordenando por hora de inicio las reservas """
    reservas_ordenadas = ordena_reservas(reservas)
    pistas = []

    for reserva in reservas_ordenadas:
        asignado = False

        for pista in pistas:
            if pista[-1][1] <= reserva[0]: # si la ultima reserva no coincide con la nueva reserva
                pista.append(reserva)
                asignado = True
                break

        if asignado == False:
            pistas.append(reserva) # crear nueva pista

    return pistas

def calcular_pistas_necesarias(reservas : list[tuple[int, int]]) -> int :
    pistas_libres = buscar_pista_libre(reservas)
    return len(pistas_libres)


res = [(10, 12), (9, 11), (11, 13), (13, 15)]
print(ordena_reservas(res))
print(buscar_pista_libre(res))
print(calcular_pistas_necesarias(res))