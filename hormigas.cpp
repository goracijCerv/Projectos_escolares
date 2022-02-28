//Implentacion del Colonia de hormigas
//J.Horacio Cervantes P
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<stdbool.h>
#include <time.h>
 int cam[7][7]={
{0,5,3,0,0,6,0},//1
{5,0,4,0,0,0,5},//2
{3,4,0,0,6,3,3},//3
{0,0,0,0,5,0,4},//4
{0,0,6,5,0,6,0},//5
{6,0,3,0,5,0,0},//6
{0,5,3,4,0,0,0}//7
};
double tao,Q,p;
int alf=1,bet=1;
double taon[7][7];
double taoss[7][7];
double n[7][7];
int camhor[8];
bool band,bandva;
void hacermats(){
    //ponemos esto porque no tenemos ni idea si esque funcionara de la otra forma dado que 
    //la feromona cambia 
    //matriz de la cosa que es n
    int x,y;
    //primero se igaula ala de camino
    for( x=0;x<7;x++){
		for( y=0;y<7;y++){
		   n[x][y]=cam[x][y];
		}
	}
	//despues se pone en modo n
    for(x=0;x<7;x++){
        for(y=0;y<7;y++){
            if(n[x][y]!=0){
                n[x][y]=1/n[x][y];
            }else{
                n[x][y]=0;
            }
        }
    }
    //aqui añadimos la feroemona del camino
    for(x=0;x<7;x++){
        for(y=0;y<7;y++){
            if(n[x][y]!=0){
                taoss[x][y]=tao;
            }else{
                taoss[x][y]=0;
            }
        }
    }
}

void caltaon(double et[7][7]){
    int i=0,j=0;
	//se calcula t*n -funcional pero como tao cambia de valor dependiendo del camino hay que modificar
	for( i=0;i<7;i++){
		for( j=0;j<7;j++){
			if(n[i][j]!=0){
				et[i][j]=pow(n[i][j],alf)*pow(taoss[i][j],bet);
			}else{
				et[i][j]=0;
			}
		}
	}
	
}
void calcam(int nodoin, double et[7][7], int itcam){
	double copfil[7];
	bandva=false;
	//copiamos la fila del nodo inicial
	for(int j=0;j<7;j++){
		copfil[j]=et[nodoin][j];
	}
	if(itcam==0){
		//sacamos pij
		double sumtn=0;
		for(int j=0;j<7;j++){
			sumtn=copfil[j]+sumtn;
		}
		for(int j=0;j<7;j++){
		  if(copfil[j]!=0){
		  	copfil[j]=copfil[j]/sumtn;
			}	
		}
		//printf("pij valores \n");
		//for(int j=0;j<7;j++){
		    ///printf("%lf ",copfil[j]);
		//}
		printf("\n");
		//hacemos el random para escoger el camino
		double cambio2=(rand() % (100 - 1 + 1)) + 1;
		cambio2=cambio2/100;
		printf("el numero random cambio2 %lf\n",cambio2);
		int select;
		//inicialisamos para buscar
		double sumu=0;
		for(int j=0;j<7;j++){
			if(copfil[j]!=0){
				sumu=sumu+copfil[j];
				if(cambio2<=sumu){
					select=j;
					break;
				}
			}
		}
		camhor[itcam+1]=select;
		//printf("el celecionado %d \n",select);
		band= false;
	}else{
	    //se eliminan nodos visitados
		for(int i=0;i<itcam;i++){
			if(copfil[camhor[i]]!=0){
				copfil[camhor[i]]=0;
			} 
		}
		//se hace la exepcion en caso que ya no ayan caminos a cuales ir
		int cont=0;
		for(int j=0;j<7;j++){
			if(copfil[j]==0){
				cont++;
			}
		}
		if(cont==7){
			//printf("ya no hay caminos dispnibles\n");
			bandva=true;
			return;
		}
		//se encuentra pij
		double sumtn=0;
		for(int j=0;j<7;j++){
			sumtn=copfil[j]+sumtn;
		}
		for(int j=0;j<7;j++){
		  if(copfil[j]!=0){
		  	copfil[j]=copfil[j]/sumtn;
			}	
		}
		//hacemos el random para escoger el camino
		double cambio2=(rand() % (100 - 1 + 1)) + 1;
		cambio2=cambio2/100;
		int select;
		//inicialisamos para buscar
		double sumu=0;
		for(int j=0;j<7;j++){
			if(copfil[j]!=0){
				sumu=sumu+copfil[j];
				if(cambio2<=sumu){
					select=j;
					break;
				}
			}
		}
		if(select==3){
		   camhor[itcam+1]=select;
		   band=true;
		}else{
		    camhor[itcam+1]=select;
		    band= false;
		}
		
	}	
}
void feromod(int chochor[8], double fermat[7][7], int chocost,int iteracam){
   double pmun=1-p; //1-p
   int i2,j2,a;
   //modificacion de la feromona base (tao*1-p)
   for(i2=0;i2<7;i2++){
       for(j2=0;j2<7;j2++){
           fermat[i2][j2]=pmun*fermat[i2][j2];
       }
   }
   //directamente evaluamos los caminos de la hormiga 
    for(a=0;a<iteracam;a++){
            if(chochor[a]!=3 && chochor[a]!=-1){
            fermat[chochor[a]][chochor[a+1]]=fermat[chochor[a]][chochor[a+1]]+(Q/chocost);
            }
    }
}
int main()
{
    srand(time(0));
    printf("Por favor ingrece el valor de Tao: ");
    scanf("%lf",&tao);
    printf("\n");
    printf("por favor ingrece el valor de Q: ");
    scanf("%lf",&Q);
    printf("\n");
    printf("por favor ingrese el valor de p: ");
    scanf("%lf",&p);
    printf("\n");
    //tao=0.1;
    //Q=1;
    //p=0.01;
    
    int a,b;
    //inicialisamos la matriz del camino de la hormiga 
    for(a=0;a<8;a++){
        camhor[a]=-1;
    }
    camhor[0]=0;//se iguala a la posicion del nido;
    hacermats();
    caltaon(taon);
   /* for(a=0;a<7;a++){
        for(b=0;b<7;b++){
            printf("%lf ",taon[a][b]);
        }
        printf("\n");
    }*/
    int it;
    //esta en dentro de otro dowhile para asegurarnos que llegue a cuatro siempre
    do{
      it=0;    
     do{
     calcam(camhor[it],taon,it);
        it++;
     }while(band!=true && bandva!=true);
     
    }while(bandva==true); 
    int costcam=0;
    //imprime el camino de la horgima y su coste
    for(a=0;a<it+1;a++){
        printf("%d ",camhor[a]+1);
            if(camhor[a]!=3){
            costcam=cam[camhor[a]][camhor[a+1]]+costcam;
            }
    }
    printf("\n");
    printf("Evaluacion del camino de la hormiga %d \n",costcam);
    feromod(camhor,taoss,costcam,it+1);
    for(a=0;a<7;a++){
        for(b=0;b<7;b++){
            printf("%lf ",taoss[a][b]);
        }
        printf("\n");
    }
    return 0;
}

