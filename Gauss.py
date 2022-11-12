class matriz:
    def __init__(self,matriz_A):
        self.listas=matriz_A
        self.filas=len(matriz_A)
        self.columnas=len(matriz_A[0])
        
    def reduccion(self, i, j): #i es el indice del renglon que se le va a multiplicar, j es el indice del renglon a cambiar
        matriz_principal=self.listas
        rengloni=matriz_principal[i]
        renglon=k*rengloni
        renglon_cambiarj=matriz_principal[j]
        renglon_cambiar=renglon_cambiar+renglon
        matriz_borrar=matriz_principal.remove(renglon_cambiarj)
        matriz_reduccion=matriz_principal.insert(j, renglon_cambiar)
        print(matriz_reduccion)
        return matriz_reduccion
        #matriz_reduccion

