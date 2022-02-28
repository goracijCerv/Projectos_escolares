import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
import scipy.linalg as la

#url= "https://aulavirtual.uaa.mx/mod/resource/view.php?id=97201"
#df = pd.read_csv(url, names=['Matematicas','Ciencias','Español','Historia','EdFisica'])


class mi_ACP():

    def __init__(self, DF = pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF

    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def DF(self):
        return self.__DF


    def CentradoReducido(self):
        X_scaled = preprocessing.scale(self.DF)
        mi_df = pd.DataFrame(X_scaled)
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                self.DF.iloc[i,j] = mi_df.iloc[i,j]
        return self.DF

    def CentroReducido1(self):
        matriz_lista = np.empty([self.num_filas, self.num_columnas])
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                a = self.DF.iloc[i,j]
                media = np.mean(self.DF.iloc[:,j])
                desviacion = np.std(self.DF.iloc[:,j])
                r = (a - media)/desviacion
                matriz_lista[i,j] = r
        return matriz_lista

    def matrizRIndividuos(self, matriz):
        A = np.matrix(matriz)
        B = np.matrix(matriz)
        T = np.transpose(A)
        producto = T * B
        R = producto/ self.num_filas
        return R

    def componentes(self, X, V):
        componentes_principales = X * V
        return componentes_principales

    def cosenosIndividuos(self, comp, matrizX):
        matriz_cosenos = np.empty([self.num_filas, self.num_columnas])
        cuadradoX = np.power(matrizX, 2)
        sumaRenglones = cuadradoX.sum(axis=1)
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                componente_cuadrado = np.power(comp, 2)
                matriz_cosenos[i,j] = componente_cuadrado[i,j]/sumaRenglones[i]
        return matriz_cosenos

    def valores_propios_var(self, matriz):
        valores_propios, vectores_propios = la.eig(matriz)
        valores_propios = valores_propios.real
        vectores_propios = vectores_propios.real
        indice_fila, indice_columna = vectores_propios.shape
        cuadrado_vectores = np.power(vectores_propios, 2)
        print("Lambda1")
        lambda1 = valores_propios[0]
        print(lambda1.real)
        print("Vecotres propios al cuadrado")
        print(cuadrado_vectores)
        cuadrado = pd.DataFrame(cuadrado_vectores)
        print(cuadrado)
        v1 = cuadrado_vectores[:,0] * valores_propios[0]
        df_v1 = pd.DataFrame(v1)
        print("v1 por lambda")
        print(df_v1)

    def matrizRVariables(self, matriz):
        A = np.matrix(matriz)
        B = np.matrix(matriz)
        T = np.transpose(B)
        producto = A*T
        R = producto/ self.num_filas
        return R

    def estadisticas(self, nc):
        media = np.mean(self.DF.iloc[:,nc])
        desviacion = np.std(self.DF.iloc[:,nc])
        dato_centrado_reducido = (self.DF.iloc[:,nc] - media)/ desviacion

        return {'Variable': self.DF.iloc[:,],
                'Media': media,
                 'DesEst': desviacion,
                 'dato_centrado_reducido' : dato_centrado_reducido}


datos_est = pd.read_csv('C:/Users/pepee.DESKTOP-K0S14SU/OneDrive/Documents/sexto semestre/IA/EjemploEstudiantes.csv', delimiter =";", decimal=",",index_col=0 )
datos = mi_ACP(datos_est)
print(datos.DF)

#Plano Principal

#Centrado reducido
matrizX = datos.CentroReducido1()
centrado_reducido = pd.DataFrame(matrizX)
print("Matriz centrada reducida")
print(centrado_reducido)

#Matriz de correlaciones
MatrizRind= datos.matrizRIndividuos(matrizX)
MatrizR = pd.DataFrame(MatrizRind)
print("Matriz de correlaciones")
print(MatrizR)

#Matriz de componentes principales

componentes_principales = datos.componentes(matrizX, MatrizRind)
print("componentes_principales")
mi_df = pd.DataFrame(componentes_principales)
print(mi_df)
X=mi_df.iloc[0:10,0:3].values
plt.scatter(X[:,0], X[:,1],s=55,c="red",label="cluster 1")

plt.title("PCA estudiantes")
plt.show()
#Matriz de cosenos cuadrados

cosenos = datos.cosenosIndividuos(componentes_principales, matrizX)
mi_df_cosenos = pd.DataFrame(cosenos)
print("Cosenos")
print(mi_df_cosenos)

#Circulo De Correlaciones

#Centrado y reducido
matrizX = datos.CentroReducido1()
print('Matriz X variables')
print(matrizX)

#Matriz de correlaciones
print('Matriz R variables')
matrizRvar = datos.matrizRVariables(matrizX)
print(matrizRvar)


datos.valores_propios_var(matrizRvar)
#https://stackabuse.com/implementing-pca-in-python-with-scikit-learn/
#https://builtin.com/data-science/step-step-explanation-principal-component-analysis
#https://towardsdatascience.com/a-complete-guide-to-principal-component-analysis-pca-in-machine-learning-664f34fc3e5a
#https://www.kindsonthegenius.com/principal-components-analysispca-in-python-step-by-step/
#https://www.datacamp.com/community/tutorials/principal-component-analysis-in-python
#https://www.gatevidyalay.com/tag/principal-component-analysis-for-dummies/