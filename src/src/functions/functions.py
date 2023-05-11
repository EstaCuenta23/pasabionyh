def comprobar_lista(lista1=None, lista2=None):
    if lista1 and lista2:
        resultado = []
        for elemento in lista1:
            if elemento in lista2:
                resultado.append(elemento)
        return resultado
    else:
        print("Error: No se ha especificado una lista")