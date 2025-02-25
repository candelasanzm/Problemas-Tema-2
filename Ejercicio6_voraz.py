HORA_INICIO = 0
HORA_FIN = 1

def ordena_reservas(reservas : list[tuple[int, int]]) -> list[tuple[int, int]] :
    """ Ordena las reservas por hora de inicio de menor a mayor """
    inicio = lambda reserva: reserva[0] # defino la funcion lambda para obtener la hora de inicio de cada reserva
    return sorted(reservas, key = inicio)

def buscar_pista_libre(reservas : list[tuple[int, int]]) -> list[tuple[int, int]]:
    """ Busca cuantas pistas necesito, ordenando por hora de inicio las reservas """
    
    # ordeno las reservas por hora de inicio 
    reservas_ordenadas = ordena_reservas(reservas)
    
    # inicializo una lista donde ire agregando las horas de finalizacion
    pistas = []

    for reserva in reservas_ordenadas:
        inicio, fin = reserva # separo los valores de la tupla

        # busco una pista que quede libre antes de que empiece una nueva reserva
        pista_asignada = False

        for i in range (len(pistas)):
            if pistas[i] <= inicio: # si la ultima reserva no coincide con la nueva reserva
                pistas[i] = fin # actualizar la hora de finalizacion de la pista que queda libre con la nueva reserva
                pista_asignada = True
                break

        if pista_asignada == False:
            pistas.append(fin) # crear nueva pista

    return len(pistas)


res = [(10, 12), (9, 11), (11, 13)]
print(ordena_reservas(res))
print(buscar_pista_libre(res))