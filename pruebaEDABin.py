import math

import numpy as np
import random

def genSolIni():
    generadorin = np.zeros((10, 2));
    for x in range(10):
        generadorin[x, 0] = random.random()
        generadorin[x, 1] = x
    ##Ordenamos el generador inicial
    generadorin = generadorin[generadorin[:, 0].argsort()]
    return  generadorin[:,1];

##Se obtiene la probabilidad de los que faltan
def PrbabilidadFaltantes(Faltantes, columna, matProbabilidades):
    listaDeProbailidadRep = np.zeros(len(Faltantes))
    probabilidadMatFaltantes = np.zeros(len(Faltantes))
    probabilidadesRep = 0;
    #Primero hay que sumar todas las probabilidades de la columna asi que hay que recorrer
    for c in range(len(Faltantes)):
        for r in range(10):
            for r2 in range(10):
                if r == columna:
                    if r2 == Faltantes[c]:
                        probabilidadesRep = probabilidadesRep + matProbabilidades[r2,r]
                        probabilidadMatFaltantes[c] = matProbabilidades[r2,r]

    for x in range(len(listaDeProbailidadRep)):
        listaDeProbailidadRep[x] = probabilidadMatFaltantes[x]/probabilidadesRep


    #hay que ordenar el vectro de menor a mayor
    listaDeProbailidadRepOrdenada= np.sort(listaDeProbailidadRep)

    #En caso que los elementos sean un nan
    contNan=0

    for k in range(len(listaDeProbailidadRepOrdenada)):
        if math.isnan(listaDeProbailidadRepOrdenada[k]):
            contNan=contNan+1

    if contNan >= 1:
        listaDeProbailidadNan = np.zeros(len(listaDeProbailidadRepOrdenada))
        probabilidadesRep = 0;
        for r in range(len(listaDeProbailidadNan)):
            if r == 0:
                listaDeProbailidadNan[r] = 1 / len(listaDeProbailidadNan);
                probabilidadesRep = probabilidadesRep + 1 / len(listaDeProbailidadNan)
            else:
                probabilidadesRep = probabilidadesRep + 1 / len(listaDeProbailidadNan)
                listaDeProbailidadNan[r] = probabilidadesRep;
        return listaDeProbailidadNan

    return listaDeProbailidadRepOrdenada;


MatPoblacion=np.zeros((30,10))
for x in range(30):
    MatPoblacion[x]=genSolIni()
print(MatPoblacion)
columnaCalif=np.zeros((30,1));
MatPoblacion=np.append(MatPoblacion,columnaCalif,axis=1)
print("Agregamos la columna de calificacion \n");
print(MatPoblacion)
pesos=np.array([3,6,2,1,5,7,2,4,1,9])
cont=0;
bin=0
for x in range(30):
    y=0;
    while(y!=10):
        pos = MatPoblacion[x, y]
        pos = int(pos)
        p = pesos[pos]
        if (p + cont) <= 10:
            cont = cont + p
            y=y+1
        else:
            bin = bin + 1
            cont = 0;
    MatPoblacion[x, 10] = bin+1
    bin = 0
print("Agregamos la calificacion \n")
print(MatPoblacion)
#Ordenamos a los mejores
MatPoblacion=MatPoblacion[MatPoblacion[:, 10].argsort()]
print("Se ordena segun los mejores \n")
print(MatPoblacion)

#Obtenmos los 15 mejores
elitismo=MatPoblacion[0:15,0:10]
print("Elitismo  \n")
print(elitismo)
#Generar nueva probabilidad
MatProbabilidad=np.zeros((10,10))
for x in range(10):
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = cTen = 0;
    for y in range(15):
        if(elitismo[y,x]==0):
            c1=c1+1;
        elif(elitismo[y,x]==1):
            c2 = c2 + 1;
        elif (elitismo[y, x] == 2):
            c3 = c3 + 1;
        elif (elitismo[y, x] == 3):
            c4 = c4 + 1;
        elif (elitismo[y, x] == 4):
            c5 = c5 + 1;
        elif (elitismo[y, x] == 5):
            c6 = c6 + 1;
        elif (elitismo[y, x] == 6):
            c7 = c7 + 1;
        elif (elitismo[y, x] == 7):
            c8 = c8 + 1;
        elif (elitismo[y, x] == 8):
            c9 = c9 + 1;
        elif (elitismo[y, x] == 9):
            cTen = cTen + 1;
    MatProbabilidad[0, x] = c1/15
    MatProbabilidad[1, x] = c2 / 15
    MatProbabilidad[2, x] = c3 / 15
    MatProbabilidad[3, x] = c4 / 15
    MatProbabilidad[4, x] = c5 / 15
    MatProbabilidad[5, x] = c6 / 15
    MatProbabilidad[6, x] = c7 / 15
    MatProbabilidad[7, x] = c8 / 15
    MatProbabilidad[8, x] = c9 / 15
    MatProbabilidad[9, x] = cTen / 15

#La matriz de Probabilidad nueva
print("Matriz de probabilidad \n")
print(MatProbabilidad)

#Nueva poblacion
#ponemos la probabilidad nueva
PoblacionOrdenacion=np.zeros((30,10))
PoblacinN=np.zeros((30,10))
for x in range(30):
    for y in range(10):
        PoblacinN[x,y]=random.random()
#Cambiar por las posiciones
#prob=MatProbabilidad[:,0]
#print()
#print(prob)
#print()
#print(prob.argsort())
#print(prob[prob.argsort()])
for x in range(10):
    prob=MatProbabilidad[:,x]
    probPos=prob.argsort()
    probOrd=prob[prob.argsort()]
    for y in range(30):
        k=0;
        while(k!=10):
            if(probOrd[k]==0):
                k=k+1;
            else:
                loqueQueda=probOrd[k:]
                loqueQuedaPos=probPos[k:]
                numerosAv=np.zeros(len(loqueQueda))
                sum=0;
                ##Se obtubo la suma de las probabilidades
                for l in range(len(loqueQueda)):
                    if l==0:
                        numerosAv[l]=loqueQueda[l];
                        sum=sum+loqueQueda[l]
                    else:
                        sum=sum+loqueQueda[l]
                        numerosAv[l]=sum;
                ##Se establecera los rangos
                for l in range(len(numerosAv)):
                    if l==0:
                        if PoblacinN[y,x] <= numerosAv[l]:
                            PoblacionOrdenacion[y,x]=loqueQuedaPos[l];
                    elif l== len(numerosAv)-1:
                        if PoblacinN[y,x] > numerosAv[l-1] and PoblacinN[y,x] <= 1:
                            PoblacionOrdenacion[y,x]=loqueQuedaPos[l]
                    else:
                        if PoblacinN[y,x] > numerosAv[l-1] and PoblacinN[y,x] <= numerosAv[l]:
                            PoblacionOrdenacion[y,x]=loqueQuedaPos[l]
                k=10;

print("Nuevos valores estadisticos")
print(PoblacinN)
print("Nuevas posiciones \n")
print(PoblacionOrdenacion)
##Tratando de quitar los valores repetidos
for x in range(30):
    sol=PoblacionOrdenacion[x,:]
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = cTen = 0;
    posRepetidos = []
    for y in range(10):
        posicion=y+1
        while(posicion !=10):
            if sol[y]==sol[posicion]:
                posRepetidos.append(posicion)

            posicion=posicion+1

    for pos in posRepetidos:
        # check if the count of sweet is > 1 (repeating item)
        if posRepetidos.count(pos) > 1:
            # if True, remove the first occurrence of sweet
            posRepetidos.remove(pos)
    #print("Los repetidos \n")
    #print(posRepetidos)

    for k in range(10):
        if (sol[k] == 0):
            c1 = c1 + 1;
        elif (sol[k] == 1):
            c2 = c2 + 1;
        elif (sol[k] == 2):
            c3 = c3 + 1;
        elif (sol[k] == 3):
            c4 = c4 + 1;
        elif (sol[k] == 4):
            c5 = c5 + 1;
        elif (sol[k] == 5):
            c6 = c6 + 1;
        elif (sol[k] == 6):
            c7 = c7 + 1;
        elif (sol[k] == 7):
            c8 = c8 + 1;
        elif (sol[k] == 8):
            c9 = c9 + 1;
        elif (sol[k] == 9):
            cTen = cTen + 1;
    Faltantes=[]
    if (c1 == 0):
        Faltantes.append(0);
    if (c2 == 0):
        Faltantes.append(1);
    if (c3 == 0):
        Faltantes.append(2);
    if (c4 == 0):
        Faltantes.append(3);
    if (c5 == 0):
        Faltantes.append(4);
    if (c6 ==0):
        Faltantes.append(5);
    if (c7 == 0):
        Faltantes.append(6);
    if (c8 == 0):
        Faltantes.append(7);
    if (c9 == 0):
        Faltantes.append(8);
    if (cTen == 0):
        Faltantes.append(9);

    #print("los faltantes\n")
    #print(Faltantes)
    for j in range(len(posRepetidos)):
        probR=random.random()
        apuntPos=posRepetidos[j]
        probaFaltantes=PrbabilidadFaltantes(Faltantes,apuntPos,MatProbabilidad)
        print(probaFaltantes)
        lol=False
        while(lol!=True):
            for l in range(len(probaFaltantes)):
                if l == 0:
                    if probR <= probaFaltantes[l]:
                        PoblacionOrdenacion[x,apuntPos] = Faltantes[l];
                        Faltantes.pop(l)
                elif l == len(probaFaltantes) - 1:
                    if probR > probaFaltantes[l - 1] and probR <= 1:
                        PoblacionOrdenacion[x,apuntPos] = Faltantes[l]
                        Faltantes.pop(l)
                else:
                    if probR > probaFaltantes[l - 1] and probR <= probaFaltantes[l]:
                        PoblacionOrdenacion[x,apuntPos] = Faltantes[l]
                        Faltantes.pop(l)

            lol=True

print("En teoria sin repeteir \n")
print(PoblacionOrdenacion)
##Hacer algo similar a la ruleta
##Se vuelve a evaluar
#columnaCalif=np.zeros((30,1));
#PoblacionOrdenacion=np.append(PoblacionOrdenacion,columnaCalif,axis=1)
#cont=0;
#bin=0
#for x in range(30):
#    y=0;
#    while(y!=10):
#        pos = PoblacionOrdenacion[x, y]
#        pos = int(pos)
#        p = pesos[pos]
#        if (p + cont) <= 10:
#            cont = cont + p
#            y=y+1
#        else:
#            bin = bin + 1
#            cont = 0;
#   PoblacionOrdenacion[x, 10] = bin+1
#    bin = 0
#print("Agregamos la calificacion \n")
#print(PoblacionOrdenacion)


