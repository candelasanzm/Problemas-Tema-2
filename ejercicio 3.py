def mejor_candidato_min(candidatos :list) -> any:
    """ Devuelve el menor candidato evaluando pares """
    if len(candidatos) == 1:
        return candidatos[0]
    
    min_candidato = 10000000
    for i in range(0, len(candidatos) - 1, 2):
        menor = min(candidatos[i], candidatos[i + 1])
        min_candidato = min(min_candidato, menor)

    if len(candidatos) % 2 == 1:
        min_candidato = min(min_candidato, candidatos[-1])

    return min_candidato

def mejor_candidato_max(candidatos :list) -> any:
    """ Devuelve el meayor candidato evaluando pares"""
    if len(candidatos) == 1:
        return candidatos[0]
    
    max_candidato = -10000000
    for i in range(0, len(candidatos) - 1, 2):
        mayor = max(candidatos[i], candidatos[i + 1])
        max_candidato = max(max_candidato, mayor)

    if len(candidatos) % 2 == 1:
        max_candidato = max(max_candidato, candidatos[-1])

    return max_candidato

def voraz(candidatos :list) -> list:
    if not candidatos:
        return None, None
    else:
        min_val = mejor_candidato_min(candidatos)
        max_val = mejor_candidato_max(candidatos)
        candidatos.remove(min_val)
        candidatos.remove(max_val)
    return min_val, max_val

v = [3, 4, 1, 7, 5, 9]
min, max = voraz(v)
print(f"Mínimo: {min}, Máximo: {max}")