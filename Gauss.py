class matriz:
    
    def __init__(self,matriz_A):
        self.listas=matriz_A
        self.filas=len(matriz_A)
        self.columnas=len(matriz_A[0])
        
    def __repr__(self):
        return str(self.listas)
    
    def reduccion(self, k, i, j): #i es el indice del renglon que se le va a multiplicar, j es el indice del renglon a cambiar, k es el número para multiplicar
        '''
        Tiene parámetros:
        k: es el número por el cual se multiplica la fila i
        i: es el indice de la fila a multiplicar
        j: es el indice de la fila a cambiar
        >>> m_1=matriz([[1,2,3],[4,5,6],[7,8,9]])
        >>> m_1
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> m_2=m_1.reduccion(4,1,2)
        >>> m_2
        [[1, 2, 3], [23, 24, 25], [7, 8, 9]]
        >>> m_3=matriz([[1,4,5],[3,6,7],[9,0,9]])
        >>> m_3
        [[1, 4, 5], [3, 6, 7], [9, 0, 9]]
        >>> m_4=m_3.reduccion(4,1,2)
        >>> m_4
        [[1, 4, 5], [21, 12, 21], [9, 0, 9]]
        >>> m_5=matriz([[1,2,2],[3,4,7],[3,6,1]])
        >>> m_5
        [[1, 2, 2], [3, 4, 7], [3, 6, 1]]
        >>> m_6=m_5.reduccion(4,1,2)
        >>> m_6
        [[1, 2, 2], [15, 18, 13], [3, 6, 1]]
        '''
        matriz_principal=self.listas
        rengloni=matriz_principal[i]
        renglon=[]
        for t in rengloni:
            renglon.append(t*k)
        renglon_cambiarj=matriz_principal[j]
        renglon_cambiar=[]
        for i in renglon_cambiarj:
            j=0
            renglon_cambiar.append(i+renglon[j])
            j=j+1
        matriz_principal[j]=renglon_cambiar
        return matriz_principal

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
