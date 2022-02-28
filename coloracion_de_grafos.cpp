/*
J.Horacio Cervantes.P
Implementacion del algoritmo de coloracion de grafos
*\
#include<bits/stdc++.h> 
using namespace std;
bool camino[15][15];
int main(){
	int vert;
	int con;
	cout<<"Ingrese la cantidad de vertices: "; cin>>vert;
	char color[vert][vert];
	for(int i=0; i<vert; i++){
		for(int j=0; j<vert; j++){
			camino[i][j]=false;
			color[i][j]='0';
		}
	}
	
	for(int x=0; x<vert; x++){
		for(int j=0; j<vert; j++){
			if(x==j){
				
			}
			else if(j<x){
				do{
					j++;
				}while(j<x);
			}
			else{
				cout<<"Incerte 1 si es que el vertice "<<x+1<<" tiene alguna conexion con el vertice "<<j+1<<endl;
				cout<<"Sino es el caso incerte cualquier otro numero"<<endl;
				cin>>con;
				if(con==1){
					camino[x][j]=true;
					camino[j][x]=true;
				}else{
				}
			}
		}
	}
	cout<<endl;
	cout<<"Matriz de adyaciencia del grafo corespondiente "<<endl;
	for(int i=0; i<vert; i++){
		for(int j=0; j<vert; j++){
			cout<<camino[i][j]<<" ";
		}
		cout<<endl;
	}
	//encontrar el que tenga mayor conexion
	int vectcon[vert];
	int max=0,min=-99;
	int cont;
	for(int a=0; a<vert; a++){
		cont=0;
		for(int b=0; b<vert; b++){
			if(camino[a][b]==true){
				cont=cont+1;
			}
		}
		vectcon[a]=cont;
		if(vectcon[a]>max){
		max=vectcon[a];
		}else if(vectcon[a]<min){
		 min=vectcon[a];
		}
	
	}
	
  
	cout<<"Cantidad de conexines de cada vertice"<<endl;
  int d6=max;
	do{
		for(int xt=0; xt<vert; xt++){
			if(vectcon[xt]==d6){
				cout<<"El vertice "<<xt+1<<" tiene esta cantidad de conexiones: "<<vectcon[xt]<<endl;
			}
		}
		d6=d6-1;
	}while(d6!=min);
	
	char coloress[vert];
	for(int a3=0;a3<vert;a3++){
  	cout<<"incerte el color numero"<<a3+1<<" solo una letra: "; cin>>coloress[a3];
	}
	int colormax,color2=0;
	int clcont=0;
	
	do{
		for(int x2=0;x2<vert;x2++){
			if(vectcon[x2]==max){
				  color2=0;
				  clcont=0;
			  while(color2<vert){
				  clcont=0;
			  	for(int j3=0; j3<vert; j3++){
			  		if(camino[x2][j3]==true && color[x2][j3]==coloress[color2]){
			  			clcont++;
						}
					}
					if(clcont==0){
						for(int j4=0; j4<vert; j4++){
							if(camino[j4][x2]==true){
								color[j4][x2]=coloress[color2];
							}
						}
						color2=vert;
					}
					else{
						color2++;
						colormax=color2;
					}
				}
			}
		}
	max=max-1;	 
	}while(max!=min);
	cout<<"La matriz de adyaciencia con colores "<<endl;
	for(int i6=0; i6<vert; i6++){
		for(int j6=0; j6<vert; j6++){
			cout<<color[i6][j6]<<" ";
		}
		cout<<endl;
	}
	cout<<"la cantidad de colores para colorear el grafo fueron: "<<colormax+1<<endl;
  int d=0,d4=0;
  while(d<vert){
  	d4=0;
		for(int d2=0;d2<vert; d2++){
  		if(camino[d2][d]==true && d4==0){
  			cout<<"El vertice "<<d+1<<" tiene el color: "<<color[d2][d]<<endl;
  			d4++;
			}			
		}
		d++;
	}
	system("pause");
	return 0;
}

