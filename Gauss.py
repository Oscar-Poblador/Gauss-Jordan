class matriz:
    
    def __init__(self,matriz_A):
        self.listas=matriz_A
        self.filas=len(matriz_A)
        self.columnas=len(matriz_A[0])
    def __repr__(self):
        return str(self.listas)
    def multiplicar(self,aux,num_fila):
        '''
        Retorna una nueva fila en la que se multiplicó el número de fila indicado por el valor de aux ingresado
        >>> m_1=matriz([1,2,3],[4,5,6],[7,8,9])

        >>> m_1
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> r_1=m_1.multiplicar(5,1)

        >>> r_1
        [[1, 2, 3], [20, 25, 30], [7, 8, 9]]
        >>> r_1=m_1.multiplicar(8,2)

        >>> r_1
        [[1, 2, 3], [4, 5, 6], [56, 64, 72]]
        >>> r_1=m_1.multiplicar(0.5,1)
        
        >>> r_1
        [[1, 2, 3], [2.0, 2.5, 3.0], [7, 8, 9]]
        '''
        renglon_multiplicar=[]
        n=[]
        m=[]
        matriz_multiplicar=[]
        for i in range(0,self.filas):
            renglon_multiplicar.append(self.listas[num_fila][i]*aux)
        for j in range(0,self.filas):
            nueva_lista=[]
            for k in range(0,self.columnas):
                nueva_lista.append(self.listas[j][k])
            matriz_multiplicar.append(nueva_lista)
        matriz_multiplicar[num_fila]=renglon_multiplicar
        return matriz_multiplicar
        
m_1=matriz([[1,2,3],[4,5,6],[7,8,9]])
print(m_1)
r_1=m_1.multiplicar(5,0)
print(r_1)
print(m_1)