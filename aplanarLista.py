
def aplanarLista(l):
    """Recibe como parámetro una lista de listas, y devuelve una lista de un nivel"""
    nuevaLista = [item for sublist in l for item in sublist]
    return nuevaLista


print(aplanarLista([[1, 2, 3], [4, 5, 6], [7], [8, 9]]))
