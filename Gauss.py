matriz_cambio=[]
class Matriz:
    def __init__(self,matriz_A):
        self.listas=matriz_A
        self.filas=len(matriz_A)
        self.columnas=len(matriz_A[0])
    def __repr__(self):
        return str(self.listas)
    
    def reduccion(self, k, i, j,matriz_entrada): #i es el indice del renglon que se le va a multiplicar, j es el indice del renglon a cambiar, k es el número para multiplicar
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
        listas=matriz_entrada
        filas=len(matriz_entrada)
        columnas=len(matriz_entrada[0])
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
    def cambiafila(self,inicio,llegada,matriz_entrada):
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
        listas=matriz_entrada
        filas=len(matriz_entrada)
        columnas=len(matriz_entrada[0])
        filaInic=listas[inicio]
        filaLleg=listas[llegada]
        matriz_B=listas[llegada]=filaInic
        matriz_B=listas[inicio]=filaLleg
        return listas

    def multiplicar(self,aux,num_fila,matriz_entrada):
        '''
        Retorna una nueva fila en la que se multiplicó el número de fila indicado por el valor de aux ingresado
        >>> m_1=matriz([[1,2,3],[4,5,6],[7,8,9]])

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
        listas=matriz_entrada
        filas=len(matriz_entrada)
        columnas=len(matriz_entrada[0])
        matriz_multiplicar=[]
        for i in range(0,columnas):
            renglon_multiplicar.append(listas[num_fila][i]*aux)
        for j in range(0,filas):
            nueva_lista=[]
            for k in range(0,columnas):
                nueva_lista.append(listas[j][k])
            matriz_multiplicar.append(nueva_lista)
        matriz_multiplicar[num_fila]=renglon_multiplicar
        return matriz_multiplicar   
class Gauss(Matriz):
    
    def gauss_jordan(self):
        print("\n------- INICIO DE SOLUCIÓN POR MÉTODO GAUSS JORDAN -------\n")
        global matriz_cambio
        #Crea una matriz que va cambiando en el proceso de solución
        for j in range(0,self.filas):
            nueva_lista=[]
            for k in range(0,self.columnas):
                nueva_lista.append(self.listas[j][k])
            matriz_cambio.append(nueva_lista)
        print("La matriz a operar es la siguiente: ",matriz_cambio)

        #Simplifica las columnas hacia abajo
        for i in range(0,self.columnas):
            self.simplificar(i,i)
            
       
    def simplificar(self,a,b):
        global matriz_cambio
        matriz_aux2=[]
        print(b)
        if(b==(self.columnas-1)):
            #De ser necesario se normaliza el primer digito a número 1 
            a-=1
            b-=1
            if(matriz_cambio[a][b]!=1):
                normalizar=1/matriz_cambio[a][b]   
                for k in range(0,self.columnas):
                    matriz_cambio[a][k]=normalizar*matriz_cambio[a][k]
            
            for j in range(0,self.filas):
                nueva_lista=[]
                for k in range(0,self.columnas):
                    nueva_lista.append(matriz_cambio[j][k])
                matriz_aux2.append(nueva_lista)
        else:
             #Si en la fila principal el vector inicia en 1 realiza el cambio de fila 
            if(matriz_cambio[a][b]==0):
                aux=0
                contador=a+1
                while(aux==0):
                    if(matriz_cambio[contador][b]==0):
                        aux=0
                        contador+=1
                    else:
                        aux=1
                matriz_cambio=super().cambiafila(a,contador,matriz_cambio)
                print("\nLa matriz necesitó un cambio de filas\n\nLa matriz resultante fue: ",matriz_cambio)
            #De ser necesario se normaliza el primer digito a número 1 
            if(matriz_cambio[a][b]!=1):
                normalizar=1/matriz_cambio[a][b]   
                for k in range(0,self.columnas):
                    matriz_cambio[a][k]=normalizar*matriz_cambio[a][k]

            #Simplifica la primera columna
            for j in range(0,self.filas):
                nueva_lista=[]
                for k in range(0,self.columnas):
                    nueva_lista.append(matriz_cambio[j][k])
                matriz_aux2.append(nueva_lista)

            inverso=0
            for j in range(a+1,self.filas):    
                inverso=matriz_cambio[j][b]*(-1)
                matriz_aux=super().multiplicar(inverso,a,matriz_cambio)
                for k in range(0,self.columnas):
                    matriz_cambio[j][k]=(matriz_cambio[j][k]+matriz_aux[a][k])
            print("\nSe simplificó la ",b, " columna")
        print("\nMatriz entrada: ",matriz_aux2,"\n")
        print("\nMatriz resultado: ",matriz_cambio,"\n")

        
#Pruebas Gauss
g_1=Gauss([[1,4,5,6,1],[8,32,7,8,2],[9,0,9,6,3],[4,9,5,1,4]])
g_1.gauss_jordan()



#Pruebas funcionamiento operaciones matriciales PARA LA VERSIÓN BETA COMENTAR LA CLASE GAUSS Y EJECUTAR PRUEBAS
# m_1=matriz([[1,4,5],[3,6,7],[9,0,9]])
# m_2=matriz([[1,2,3],[4,5,6],[7,8,9]])
# m_3=matriz([[1,2,2],[3,4,7],[3,6,1]])
# print(m_1)
# m_1.reduccion(4,1,2)
# m_3.reduccion(4,1,2)
# m_5.reduccion(4,1,2)
# r_1=m_1.multiplicar(2,0)
# print(r_1)
# print(m_1)
#r_2=m_1.cambiafila(0,1)
