def ordenar_reservas (reservas : list[tuple[int, int]]) -> list[tuple[int, int]] : 
    """ Ordena las reservas por hora de inicio """
    for i in range (len(reservas)) :
        for j in range (i + 1, len(reservas)) :
            if reservas[i][0] > reservas[j][0] :
                reservas[i], reservas[j] = reservas[j], reservas[i] # si la reserva en la posicion i es mayor que la de la posicion j las cambio de orden para ordenar de menor a mayor las reservas
    return reservas

def buscar_pista_libre(pistas : list[int], inicio : int) -> int:
    """ Busca una pista libre cuya hora de fin sea menor o igual de que la de inicio"""
    for i in range (len(pistas)) :
        if pistas[i] <= inicio :
            return i
    return -1

def num_min_pistas(reservas : list[tuple[int, int]]) -> int:
    """ Calcula el numero minimo de pistas necesarias para que se puedan realizar todas las reservas sin problemas """
    reservas = ordenar_reservas(reservas)

    pistas_final = []

    for reserva in reservas:
        inicio, fin = reserva
        pista_libre = buscar_pista_libre(pistas_final, inicio)

        if pista_libre != -1 :
            pistas_final[pista_libre] = fin

        else :
            pistas_final.append(fin)

    return len(pistas_final)

reservas = [(10, 12), (9, 11), (11, 13)]
print(num_min_pistas(reservas))