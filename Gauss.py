class matriz:
    
    def __init__(self,matriz_A):
        self.listas=matriz_A
        self.filas=len(matriz_A)
        self.columnas=len(matriz_A[0])
    def __repr__(self):
        return str(self.listas)
    def multiplicar(self,aux,num_fila):
        renglon_multiplicar=[]
        for i in range(0,self.filas):
            renglon_multiplicar[i]=self.listas[num_fila]*aux
        return renglon_multiplicar
        '''
        >>> m_1=matriz([1,2,3],[4,5,6],[7,8,9])
        '''
m_1=matriz([[1,2,3],[4,5,6],[7,8,9]])
print(m_1)
#r_1=m_1.multiplicar(2,0)