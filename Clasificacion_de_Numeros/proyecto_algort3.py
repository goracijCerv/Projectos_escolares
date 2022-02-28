import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report,confusion_matrix
import matplotlib.pyplot as pl
#visualizando datos
datos=pd.read_csv("C:/Users/pepee.DESKTOP-K0S14SU/OneDrive/Documents/sexto semestre/IA/numeros.csv").to_numpy()
#Selecion de los datos
X=datos[0:,1:]
Y=datos[0:,0];
#slecion de los datos de entramiento y prueba
X_entrenamiento,X_prueba,Y_entrenamiento,Y_prueba=train_test_split(X,Y,test_size=0.5,random_state=4);
#visulizando la precicion del modelo para k vecinos con finalidad de selecionar el mejor
from sklearn import metrics
rango_k=range(1,14)
presiciones={}
lista_presiciones=[]
for k in rango_k:
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_entrenamiento,Y_entrenamiento)
    predicion=knn.predict(X_prueba)
    presiciones[k]=metrics.accuracy_score(Y_prueba,predicion)
    lista_presiciones.append(metrics.accuracy_score(Y_prueba,predicion))
#graficnado la precicion dependiendo la cantidad de k vecinos
pl.plot(rango_k,lista_presiciones)
pl.xlabel('valor de k en rango de k')
pl.ylabel('precicion de la prueba')
pl.show()
#creacion del modelo final
knn2=KNeighborsClassifier(n_neighbors=5)
knn2.fit(X_entrenamiento,Y_entrenamiento)
predicion=knn2.predict(X_prueba)
print(confusion_matrix(Y_prueba,predicion))
print(classification_report(Y_prueba,predicion));
for n in range(0,15):
    d=X_prueba[n]
    d.shape=(28,28)
    pl.imshow(255 - d, cmap='gray')
    pl.title('predicion:'+str(predicion[n]))
    pl.show()