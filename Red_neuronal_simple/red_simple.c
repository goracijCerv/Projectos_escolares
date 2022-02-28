#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<stdbool.h>
#include <time.h>
double errk6;//error de la salida
double errj4y5[2];
double oj[3];//salidas de las neuornas, 0 seria la cutro y asi
double ij[3];//donde se almaceneran las entradas de las neuronas, 0 seria la cuatro y asi
double w4y5[2][3]={
	{0.2,0.4,-0.5},//4
	{-0.3,0.1,0.2}//5
	}; //pesos que iran diriguidos a la neurona 4 //pesos que iran diriguidos a la nuerona 5
//en la primera fila seran los pesos de 4 ordenados de 1,2,3
//en la sefunda fila seran los pesos de 5 ordenados de 1,2,3
double w6[2]={-0.3,-0.2};//pesos de nuuerona 6
double thet[3]={-0.4,0.2,0.1};//valores de tehta 4,5,6
double l=0.9;//nivel de aprendizaje
int x[3]={1,0,1};//entradas
void calerr();
void actw();
int main(){
	int i,j;
	int etap=0;
	double cont;
	bool bandera=false;
	while(bandera==false ){
	  //calculando entradas de 4 y 5
	  for(i=0;i<2;i++){
	  	cont=0;
	  	for(j=0;j<3;j++){
	  		//primero se suma el peso por la entrada
	  		cont=(x[j]*w4y5[i][j])+cont;
			}
			//se suma su corespondeinte theta
			cont=cont+thet[i];
			ij[i]=cont;
			//calculando salida de 4 y 5
			oj[i]=1/(1+exp(-1*ij[i]));
		}
		//calculando entrada de 6
		cont=0;
		for(i=0;i<2;i++){
			cont=(oj[i]*w6[i]) + cont;
		}
		cont=cont+thet[2];
		ij[2]=cont;
		//calculando salida de 6
		oj[2]=1/(1+exp(-1*ij[2]));
		if(oj[2]>=.9999 || oj[2]==1){
			bandera=true;
		}else{
			calerr();
			actw();
			etap++;
		}
		
		
	}
	printf("\n");
	printf("salida de la red: %lf\n",oj[2]);
	errk6=oj[2] *(1-oj[2]) * (1-oj[2]);
	printf("el error es de: %lf",errk6);
	printf("\n");
	 for(i=0;i<2;i++){
		      for(j=0;j<3;j++){
			    printf("pesos de w%d%d:%lf \n",j+1,i+4,w4y5[i][j]);
		      }
		      printf("\n");
	     }
	     for(i=0;i<2;i++){
		   printf("peso w%d6: %lf\n",i+4,w6[i]);
	     }
	     printf("\n");
	     for(i=0;i<3;i++){
		   printf("theta(bais)%d: %lf\n",i+4,thet[i]);
	     }
	 printf("\n");
	 printf("epocas realizadas: %d",etap);    
	return 0;
}
void calerr(){
	int i;
	//calculando el error en la salida de la red
	errk6=oj[2] *(1-oj[2]) * (1-oj[2]);
	for(i=0;i<2;i++){
		//calculando el error de la neurona 4 y 5 
		errj4y5[i]=oj[i] *(1-oj[i])*errk6*w6[i];
		//printf("errorj %d: %lf \n",i+1,errj4y5[i]);
	}
	//printf("error de 6: %lf\n",errk6);
}
void actw(){
	//realizando la actualizacion de los pesos primero todo lo relazionado a la neurona 4 y despues de 5
	int x2,y;
	for(x2=0;x2<2;x2++){
		for(y=0;y<3;y++){
			w4y5[x2][y]= w4y5[x2][y] + (l*errj4y5[x2]*x[y]);
		}
		//realizando acrualizacion en los pesos de 6
		w6[x2]=w6[x2]+(l*errk6*oj[x2]);
	  //acrualizacion de las thetas 4 y 5
	  thet[x2]=thet[x2]+(l*errj4y5[x2]);
	}
	//actualizacion de theta 6
	thet[2]=thet[2]+(l*errk6);
}
