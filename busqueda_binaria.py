def busqueda_binaria(lista, objetivo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(lista) - 1
    
    if izquierda > derecha:
        return -1  
    
    medio = (izquierda + derecha) // 2
    
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria(lista, objetivo, izquierda, medio - 1)

lista_ordenada = [1, 3, 5, 7, 9, 11]
objetivo = 7
indice = busqueda_binaria(lista_ordenada, objetivo)
print(f"El número {objetivo} está en el índice {indice}.")