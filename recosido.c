#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<stdbool.h>
#include <time.h>
//J.Horacio Cervantes.P
// 3/11/2020
//universidad autonoma de aguascalientes
//Implementacion del recosido simulado 
bool conexiones[7][7]={
{0,1,1,0,0,0,1},//1
{1,0,1,1,0,0,0},//2
{1,1,0,1,1,0,1},//3
{0,1,1,0,1,1,0},//4
{0,0,1,1,0,1,1},//5
{0,0,0,1,1,0,1},//6
{1,0,1,0,1,1,0}//7
};
int coste[7][7]={
{0,12,10,0,0,0,12},//1
{12,0,8,12,0,0,0},//2
{10,8,0,11,3,0,9},//3
{0,12,11,0,11,10,0},//4
{0,0,3,11,0,6,7},//5
{0,0,0,10,6,0,9},//6
{12,0,9,0,7,9,0}//7
};
int camino[8]={0,1,2,3,4,5,6,0};
int auxcam[8];
int evaluarcam(int cam[8]){
    int j,cont2=0;
    for(j=0; j<7; j++){
     	if(coste[cam[j]][cam[j+1]]!=0){
     	    cont2=coste[cam[j]][cam[j+1]]+cont2;
     	}
	 }
   return cont2;	 
}
void cambiarcam(int cam[8]){
	int cambio1,cambio2,i,j,cont,x4,aux,aux2;
	bool bancam;
	bancam=false;
	do{
	 for(i=0;i<8;i++){
	    auxcam[i]=cam[i];
	 }
	 cambio1=(rand() % (5 - 1 + 1)) + 1;
	 //printf("cambio1 %d \n",cambio1);
	 aux2=cambio1+1;
	 cambio2=(rand() % (6 - aux2 + 1)) + aux2;
	 //printf("cambio2 %d \n",cambio2);
	 if(cambio1==cambio2  || cambio1==1 && cambio2==6){
	  do{
		cambio2=(rand() % (6 - aux2 + 1)) + aux2;
		//printf("a se trabo valio gerber \n");
	   }while(cambio1==cambio2 || cambio1==1 && cambio2==6);
	 }
	  int aux12=cambio2;
    int aux21=auxcam[cambio1];
    for(i=cambio1; i<=cambio2; i++){
        auxcam[i]=cam[aux12];
      aux12--;
    }
    auxcam[cambio2]=aux21;
     //printf("Camino que en teoria sirve \n");
    //for(x4=0;x4<8;x4++){
     //  printf("%d ",auxcam[x4]+1);
    //}
    //printf("\n");
     cont=0;
     for(j=0; j<7; j++){
     	if(conexiones[auxcam[j]][auxcam[j+1]]==true){
     	    cont++;
     	}
	 }
	 //printf("GG contador %d",cont);
	 if(cont==7){
	 	bancam=true;
	 }
	}while(bancam!=true);

}
int main(){
    srand(time(0));
    int a,ifi;
    int auxK,Ei,k,Ej;
    double T0,Tf,alf,p,K;
    double jam,jam2,vex,ver;
    printf("Incerte la temperatura inicial (T0)\n");
    scanf("%lf",&T0);
    printf("Incerte la temperatura final (Tf)\n");
    scanf("%lf",&Tf);
    printf("Incerte el valor de alfa\n");
    scanf("%lf",&alf);
    printf("Incerte el valor de p\n");
    scanf("%lf",&p);
    printf("Incerte el valor de K\n");
    scanf("%lf",&K);
    do{
       k=0;
        while(k!=K){
          Ei=evaluarcam(camino);
          //printf("Ei %d\n",Ei);
          cambiarcam(camino);
          //printf("Salio \n");
          Ej=evaluarcam(auxcam);
          //printf("Ej %d\n",Ej);
          if(Ej<Ei){
            for(a=0;a<8;a++){
             camino[a]=auxcam[a];   
            }
            for(a=0;a<8;a++){
             auxcam[a]=0;   
            }
             k++;
          }else{
           jam2=(rand() % (100 - 1 + 1)) + 1;
           jam=jam2/100;
           vex=(Ei-Ej)/T0;
           if(jam<exp(vex)){
            for(a=0;a<8;a++){
             camino[a]=auxcam[a];   
            }
            for(a=0;a<8;a++){
             auxcam[a]=0;   
            }
            k++;
          }
       }
      };
     
       // printf("Sale del interno\n");
        //printf("T0 antes %lf \n",T0);
        T0=alf*T0;
        //printf("T0 despues %lf \n",T0);
        K=p*K;
        auxK=K;
        ver=K-auxK;
        if(ver<0.5){
            K=auxK;
        }else if(ver>=0.5){
            auxK=auxK+1;
            K=auxK;
        }
        k=0;
    }while(Tf<=T0);
    printf("En teoria el mejor camino \n");
    for(a=0;a<8;a++){
    printf(" %d ",camino[a]+1);   
    }
    printf("\n");
    ifi=evaluarcam(camino);
    printf("Su coste es de %d \n",ifi);
    system("pause");
		return 0;
}
