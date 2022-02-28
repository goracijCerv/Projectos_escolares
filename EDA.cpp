//J.Horacio Cervantes.P
//Implementacion de un EDA para el problema de //OneMAX
#include<stdlib.h>
#include<stdio.h>
#include<bits/stdc++.h>
#include<time.h>
#include<iostream>
using namespace std;
int aux_matz[15][10];
int mat_p[30][10];
float mat_rand[30][10];
int calif[30];
int may,men;
float p_cero[10];
#define ind_c 30
#define cad 10
//funciones
void genpob();
void imp_pob();
void fitnes();
void elitms();
void gen_npob();
int main(){
	srand(time(NULL));
	int gen=0;
	genpob();
	cout<<"generacion "<<gen+1<<endl;
	fitnes();
	imp_pob();
	do{
		elitms();
		gen_npob();
		fitnes();
		gen=gen+1;
		cout<<"generacion "<<gen+1<<endl;
		imp_pob();
	}while(gen<20);
}

void genpob(){
	float alt,num;
	for(int i=0; i<ind_c; i++){
		for(int j=0; j<cad; j++){
			num = 1 + rand() % (1001 - 1);
			alt=num/1000;
			mat_rand[i][j]=alt;
		}
	}
	
	for(int i=0; i<ind_c; i++){
		for(int j=0; j<cad; j++){
			if(mat_rand[i][j]>0.5){
				mat_p[i][j]=1;
			}else{
				mat_p[i][j]=0;
			}
		}
	}
	
}

void imp_pob(){
	for(int i=0; i<ind_c; i++){
		cout<<"[ ";
		for(int j=0; j<cad; j++){
			cout<<mat_p[i][j]<<" ";
		}
		cout<<"]"<<" el fitnes: "<<calif[i]<<endl;
	}

} 

void fitnes(){
	men=100,may=-9;
	int cont;
	for(int i=0; i<ind_c; i++){
		cont=0;
		for(int j=0; j<cad; j++){
			if(mat_p[i][j]==1){
				cont++;
			}
		}
		calif[i]=cont;
		if(cont>may){
			may=cont;
		}else if(cont<men){
			men=cont;
		}
	}
}

void elitms(){
	//obtenemos a los quince mejores
	int x=0;
	do{
		for(int i=0; i<ind_c; i++){
			if(calif[i]==may){
				for(int j=0; j<cad;j++){
					aux_matz[x][j]=mat_p[i][j];
				}
				x=x+1;
			}
		}
		may=may-1;;
	}while(x<15);
	//contar ceros por columna para sacar el porcentaje p_cero
	int cont;
	for(int i=0; i<cad; i++){
		cont=0;
		for(int j=0; j<15; j++){
			if(aux_matz[j][i]==0){
				cont++;
			}
		}
		p_cero[i]=(cont*100)/15;
		p_cero[i]=p_cero[i]/100; //para tenerlo en porcentaje
	}
	
	
}

void gen_npob(){
	float alt,num;
	for(int i=0; i<ind_c; i++){
		for(int j=0; j<cad; j++){
			num = 1 + rand() % (1001 - 1);
			alt=num/1000;
			mat_rand[i][j]=alt;
		}
	}
	
	for(int i=0; i<cad; i++){
		for(int j=0; j<ind_c; j++){
			if(mat_rand[j][i]>p_cero[i]){
				mat_p[j][i]=1;
			}else{
				mat_p[j][i]=0;
			}
		}
	}
}
