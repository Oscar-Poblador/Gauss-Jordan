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
    def cambiafila(self,inicio,llegada):
        '''
        Cambiafila cambio de posicion dos filas inicio a llegada y viceversa
        ----------------
        >>> m1=matriz([[3,1,2],[4,5,6],[3,7,9]])
        
        >>> m1
        [[3, 1, 2], [4, 5, 6], [3, 7, 9]]
        >>> m2=m1.cambiafila(0,1)
        
        >>> m2
        [[4, 5, 6], [3, 1, 2], [3, 7, 9]]
        >>> m3=m1.cambiafila(1,2)
        
        >>> m3
        [[4, 5, 6], [3, 7, 9], [3, 1, 2]]
        >>> m4=m1.cambiafila(0,2)
        
        >>> m4
        [[3, 1, 2], [3, 7, 9], [4, 5, 6]]
        '''
        filaInic=self.listas[inicio]
        filaLleg=self.listas[llegada]
        matriz_B=self.listas[llegada]=filaInic
        matriz_B=self.listas[inicio]=filaLleg
        return self.listas

m_1=matriz([[1,2,3],[4,5,6],[7,8,9]])
print(m_1)
#r_1=m_1.multiplicar(2,0)
#m2=m_1.cambiafila(0,1)
#m2
#m3=m_1.cambiafila(1,2)
#m3
#m4=m_1.cambiafila(0,2)
#m4
