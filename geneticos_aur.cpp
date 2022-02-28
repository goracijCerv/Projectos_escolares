/*
J.Horacio Cervantes.P
Implementacion del problema oneMax con un algoritmo Genetico y elitismo
*\
#include<bits/stdc++.h> 
#include <time.h>
using namespace std;
bool poblacion[30][10];
bool aux[30][10];
int calif[30];
int may,men,posel1,posel2,poshijo,poshijo2;
int probcruz,probmut;
int califto,x3;
int gen=0;
double porcen;
void generarpob(bool pobla[30][10]){

	int numero_alt;
	for(int i=0; i<30; i++){
		for(int j=0; j<10;j++){
		 	numero_alt=(rand() % (1-0+1))+0;
		 	if(numero_alt==1){
		 		poblacion[i][j]=true;
			 }
			 else{
			 	poblacion[i][j]=false;
			 }
		}
	}
}
void imprimir(bool pobla[30][10],int x){
	cout<<"Generacion: "<<gen<<endl;
	if(gen==0 || gen==x){
		for(int i=0; i<30; i++){
		for(int j=0; j<10; j++){
			cout<<" "<<pobla[i][j]<<" ";
		}
		cout<<endl;
	}
	}
	cout<<"El porcentaje de calificacion de la poblacion es: "<<porcen<<endl;
	cout<<"El mejor de la poblacion es el individuo "<<posel1+1<<endl;
	for(int i2=0; i2<30; i2++){
		for(int j2=0; j2<10; j2++){
			if(i2==posel1){
				cout<<" "<<pobla[i2][j2]<<" ";
			}	
		}
	}
	cout<<endl;
}
void evaluar(){
	int cont=0;
	califto=0;
	may=0;
	men=-9;
	for(int i=0; i<30; i++){
		cont=0;
		for(int j=0; j<10; j++){
			if(poblacion[i][j]==true){
				cont++;
				califto++;
			}
		}
		calif[i]=cont;
		if(calif[i]>may){
		may=calif[i];
		}else if(calif[i]<men){
		 men=calif[i];
		}
	}
	porcen=califto/30;
}
void elitismo(){
	//encontrando a los elites
	int max=may;
	int min=men;
	int elit=0;
	do{
		for(int xt=0; xt<30; xt++){
			if(calif[xt]==max){
				if(elit==0){
					posel1=xt;
					elit++;
				}else if(elit==1){
					posel2=xt;
					elit++;
				}
			}
		}
		max=max-1;
	}while(elit!=2||max!=min);
	//pasar los elites a la sig poblacion
	for(int i=0; i<30; i++){
		for(int j=0; j<10; j++){
			if(i==posel1){
				aux[0][j]=poblacion[i][j];
			}
			else if(i==posel2){
				aux[1][j]=poblacion[i][j];
			}
		}
	}
}
void hijos(){
    x3=2;
	int cont;
	int canth=0;
	int r2,califf=0;
	int r3,corte,e1,e2;
	//cout<<"califto"<<califto<<endl;
	do{
	   cont=0;
	 while(cont!=2){   
	    r2=(rand() % (califto-1+1))+1;
	   // cout<<"rand "<<r2<<endl;
	    for(int i=0; i<30; i++){
	        
	        for(int j=0; j<10; j++){
	            
	            if(poblacion[i][j]==true){
	                califf++;
	                if(califf>=r2){
	                    if(cont==0){
	                        poshijo=i;
	                        califf=0;
	                        break;
	                       
	                    }else{
	                        poshijo2=i;
	                        califf=0;
	                        break;
	                        
	                    }
	                    
	                }
	               
	            }
	            
	        }
	        
	    }
	  cont++;
	  x3=x3+1;
	  //cout<<"x3 "<<x3<<endl;
	 }
	 e1=x3-2;
	 e2=x3-1;
	 //cout<<"e1 "<<e1<<endl;
	 //cout<<"e2 "<<e2<<endl;
	 r3=(rand() % (100-0+1))+0;
	 if(r3<=probcruz){
		corte=(rand() % (9-0+1))+0;
		for(int i4=0; i4<corte; i4++){
			aux[e1][i4]=poblacion[poshijo][i4];
			aux[e2][i4]=poblacion[poshijo2][i4];
		}
		for(int j4=corte; j4<10; j4++){
			aux[e1][j4]=poblacion[poshijo2][j4];
			aux[e2][j4]=poblacion[poshijo][j4];
		}
	}else{
		for(int i24=0; i24<10; i24++){
			aux[e1][i24]=poblacion[poshijo][i24];
			aux[e2][i24]=poblacion[poshijo2][i24];
		}
	}
	 canth++;
	}while(canth!=14);	    
	//cout<<"copia aux"<<endl;
	//imprimir(aux);
}

void mutacion(){
	int r5,bitr;
	for(int i=0; i<30; i++){
	r5=(rand() % (100-0+1))+0;
	bitr=(rand() % (9-0+1))+0;
	 for(int j=0; j<10; j++){
	 	if(r5<=probmut){
	 		if(j==bitr){
	 			if(aux[i][j]==false){
	 				aux[i][j]=true;
				 }else{
				 	aux[i][j]=false;
				 }
			 }
		 }
	 }
	}
}
 void recet(){
 	
 	for(int i=0; i<30; i++){
 		for(int j=0; j<10; j++){
 			poblacion[i][j]=aux[i][j];
		 }
	 }
  for(int i=0; i<30; i++){
 		for(int j=0; j<10; j++){
 			aux[i][j]=false;
		 }
	 }
	 gen++;	 
 }
 int main(){
    srand(time(0));
 	int generaciones,cont32;
	generarpob(poblacion);
 	evaluar();
 	elitismo();
 	imprimir(poblacion,0);
 	cout<<"incertar la probalidad de cruzamiento rango de 0 a 100 "<<endl;
 	cin>>probcruz;
 	cout<<"incertar la probalidad de mutacion de rango de 0 a 100 "<<endl;
 	cout<<"notece que cien seria 100% y asi"<<endl;
 	cin>>probmut;
 	cout<<"cantidad de generaciones "<<endl;
 	cin>>generaciones;
 	cont32=generaciones;
 	do{
 		hijos();
 		mutacion();
 		recet();//aqui ya tenemos nueva poblacion
		evaluar();
 		elitismo();
 		imprimir(poblacion,cont32);
	 }while(gen!=generaciones);
	 system("pause");
 	return 0;
 }
