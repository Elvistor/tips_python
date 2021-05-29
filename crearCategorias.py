def crearCategorias(l):
    """Recibe como parámetro una lista de 1 - 5, y lo categoriza Bad - Neutral - Good"""
    l = ["Good" if i>=4 else "Neutral" if i==3 else "Bad" for i in l]
    return l

print(crearCategorias([1,2,3,4,5,4,3,2,1]))