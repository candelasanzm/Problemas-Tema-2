hora_inicio = 0
hora_fin = 1

def ordena_horas(horas : list[tuple[int, int]]) -> list[tuple[int, int]] :
    """ Ordena las horas por hora de inicio de menor a mayor """
    inicio = lambda hora: hora[hora_inicio]
    return sorted(horas, key = inicio)

reservas = [(10, 12), (9, 11), (11, 13)]
print(ordena_horas(reservas))