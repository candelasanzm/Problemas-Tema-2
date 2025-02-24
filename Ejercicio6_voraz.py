HORA_INICIO = 0
HORA_FIN = 1

def ordena_reservas(reservas : list[tuple[int, int]]) -> list[tuple[int, int]] :
    """ Ordena las reservas por hora de inicio de menor a mayor """
    inicio = lambda reserva: reserva[0] # defino la funcion lambda para obtener la hora de inicio de cada reserva
    return sorted(reservas, key = inicio)

def buscar_pista_libre(reservas : list[tuple[int, int]], hora_inicio : int, hora_fin : int) -> list[tuple[int, int]]:
    """ Busca una pista libre, ordenando por hora de inicio las reservas """
    reservas_ordenadas = ordena_reservas(reservas)
    pista_libre = []
    actual = hora_inicio # variable que se va actualizando en funcion de la hora de fin de cada reserva

    for reserva in reservas_ordenadas:
        if reserva[0] >= actual and reserva[1] <= hora_fin: # si la hora de inicio de la reserva es mayor o igual a la guardada en la variable actual y menor o igual a la hora de fin
            pista_libre.append(reserva) # añadimos la reserva a la lista de pistas libres
            actual = reserva[1] # actualizo la hora actual con la hora final de la reserva

    return pista_libre

res = [(10, 12), (9, 11), (11, 13), (13, 15)]
print(ordena_reservas(res))
hora_inicio = 9
hora_fin = 15
print(buscar_pista_libre(res, hora_inicio, hora_fin))