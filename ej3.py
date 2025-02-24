def mejor_candidato_min(candidatos: list) -> any:
    """ Devuelve el menor candidato evaluando pares en O(3n/2) comparaciones """
    if len(candidatos) == 1:
        return candidatos[0]

    min_candidato = float('inf')
    
    for i in range(0, len(candidatos) - 1, 2):
        if candidatos[i] < candidatos[i + 1]:
            menor = candidatos[i]
        else:
            menor = candidatos[i + 1]
        
        min_candidato = min(min_candidato, menor)

    if len(candidatos) % 2 == 1:  # Si hay un elemento extra
        min_candidato = min(min_candidato, candidatos[-1])

    return min_candidato

def mejor_candidato_max(candidatos: list) -> any:
    """ Devuelve el mayor candidato evaluando pares en O(3n/2) comparaciones """
    if len(candidatos) == 1:
        return candidatos[0]

    max_candidato = float('-inf')

    for i in range(0, len(candidatos) - 1, 2):
        if candidatos[i] > candidatos[i + 1]:
            mayor = candidatos[i]
        else:
            mayor = candidatos[i + 1]
        
        max_candidato = max(max_candidato, mayor)

    if len(candidatos) % 2 == 1:  # Si hay un elemento extra
        max_candidato = max(max_candidato, candidatos[-1])

    return max_candidato

def voraz(candidatos: list) -> tuple:
    """ Algoritmo voraz que encuentra el mínimo y máximo en O(3n/2) comparaciones """
    if not candidatos:
        return None, None
    elif len(candidatos) == 1:
        return candidatos[0], candidatos[0]

    min_val = mejor_candidato_min(candidatos)
    max_val = mejor_candidato_max(candidatos)

    return min_val, max_val

v = [3, 4, 1, 7, 5, 9]
min, max = voraz(v)
print(f"Mínimo: {min}, Máximo: {max}")