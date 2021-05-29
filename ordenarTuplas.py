#Ordenar una lista de tuplas por elemento
def ordenar_lista(l):
    """Recibe una lista de tuplas de dos elementos y las ordena tomando como referencia el segundo elemento"""
    #Define t como clave
    l = sorted(l, key=lambda t: t[1])
    return l

print(ordenar_lista([(1,2), (4,6), (5,1), (1,0)]))