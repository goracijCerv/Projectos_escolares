import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report,confusion_matrix
import matplotlib.pyplot as pl
#usando arboles de deciciones
datos=pd.read_csv("C:/Users/pepee.DESKTOP-K0S14SU/OneDrive/Documents/sexto semestre/IA/numeros.csv").to_numpy()
#Selecion de los datos
X=datos[0:,1:]
Y=datos[0:,0];
#Entranamiento de los datos
X_entrenamiento,X_prueba,Y_entrenamiento,Y_prueba=train_test_split(X,Y,test_size=0.5);
cls=DecisionTreeClassifier()
cls.fit(X_entrenamiento,Y_entrenamiento)
predicion=cls.predict(X_prueba)
print(confusion_matrix(Y_prueba,predicion))
print(classification_report(Y_prueba,predicion));
print(predicion)
for n in range(0,15):
    d=X_prueba[n]
    d.shape=(28,28)
    pl.imshow(255 - d, cmap='gray')
    pl.title('predicion:'+str(predicion[n]))
    pl.show()