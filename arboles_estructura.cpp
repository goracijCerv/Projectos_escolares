//Implementacion de la estructura computacional (arbol)
//J.Horacio C.P
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<iostream>
using namespace std;
struct nodo{
int data;
nodo *derecho;
nodo *izquierdo;	
nodo *owl;
bool vistitado;
int nivel;
};
struct nodoc{
	int dato;
	int nivel2;
	struct nodoc *siguiente;
};
typedef struct nodoc *NODOC;
nodoc *inicio=NULL,*ult=NULL,*inicio2=NULL,*ult2=NULL;
typedef struct nodo *NODO;
NODOC getnodoC(int xs,int niv);
NODOC getnodoC2(int xs2);
void enlazarC2(NODOC alch2);
void enlazarC(NODOC alch);
int n_colas=0;
void imprimir(int bus);
void imprimirpila();
void eliminar();
int n_pila=0;
//Arboles
nodo *raiz=NULL;
NODO crear(int oka,NODO padre);
void incertar(NODO &arbol,int x,NODO padre01);
void mostrar(NODO arbol1,int cont);
bool buscar(NODO arbol2,int B);
void preorden(NODO arbol0);
void inorden(NODO arbol01);
void postorden(NODO arbol02);
void eliminar(NODO X, int obx);
void eliminarnodo(NODO elminar);
NODO izquierdo(NODO arbol03);//determina el lado izquierdo para poder eliminar
void sustituir(NODO arbol04, NODO remplazo);
void niveles(NODO arbol23);
void pro(int busquedam, NODO pp);
int cant=0;
int raizdata;
int main(){
	int op,cont=0, numero,Bn;
	do{
		cout<<"\tMenu"<<endl;
		cout<<"****************************"<<endl;
		cout<<"1- Incertar nodo"<<endl;
		cout<<"2- Mostrar arbol"<<endl;
		cout<<"3- Buscar dato en el arbol"<<endl;
		cout<<"4- Preorden"<<endl;
		cout<<"5- Inorden"<<endl;
		cout<<"6- Postorden"<<endl;
		cout<<"7- Eliminar nodo"<<endl;
		cout<<"8- Profundidad"<<endl;
		cout<<"9- Niveles"<<endl;
		cout<<"10- Salir"<<endl;
		cout<<"Opcion :";
		cin>>op;
		switch(op){
			case 1:{
				cout<<endl;
				cout<<"incerte dato :"<<endl;
				cin>>numero;
				incertar(raiz,numero,NULL);
				system("pause");
				break;
			}
			case 2:{
				cout<<"\tMostrando Arbol"<<endl;
				cout<<endl;
				mostrar(raiz,cont);
				cout<<endl;
				system("pause");
				break;
			}
			case 3:{
				cout<<endl;
				cout<<"Ingrese el dato a buscar :";
				cin>>Bn;
				bool F=buscar(raiz,Bn);
				if(F==true){
					cout<<"El numero se encuetra en el arbol"<<endl;
				}
				else{
					cout<<"El numero no se encuentra en el arbol"<<endl;
				}
				system("pause");
				break;
				
			}
			case 4:{
				cout<<endl;
				cout<<"\t Mostrando en Preorden"<<endl;
				preorden(raiz);
				system("pause");
				break;
			}
			case 5:{
				cout<<endl;
				cout<<"\t Mostrando en Inorden"<<endl;
				inorden(raiz);
				system("pause");
				break;
			}
			case 6:{
				cout<<endl;
				cout<<"\t Mostrando en Postorden"<<endl;
				postorden(raiz);
				system("pause");
				break;
			}
			case 7:{
				int f;
				cout<<"incerte el dato a eliminar"<<endl;
				cin>>f;
				eliminar(raiz,f);
				system("pause");
				break;
			}
			case 8:{
				int gg;
					cout<<"incerte el elemento a buscar"<<endl;
					cin>>gg;
					pro(gg,raiz);
					imprimirpila();
					system("pause");
				break;
			}
			case 9:{
				niveles(raiz);
				int by;
				cout<<"elemto a buscar: "; 
				cin>>by;
				imprimir(by);
				
				system("pause");
				break;
			}
			case 10:{
				cout<<endl;
				cout<<"Saliendo...."<<endl;
				system("pause");
				break;
			}
			default:{
				cout<<"shinobi execution"<<endl;
				cout<<"Yoku dekita okami"<<endl;
				
				break;
			}
		}
		system("cls");
	}while(op!=10);
}
NODO crear(int oka,NODO padre){
	NODO p = new nodo();
	p->data=oka;
	p->derecho=NULL;
	p->izquierdo=NULL;
	p->owl=padre;
	p->nivel=0;
	p->vistitado=false;
	cant=cant+1;
	n_pila=n_pila+1;
	return p;
}
void incertar(NODO &arbol,int x,NODO padre01){
	if(arbol==NULL){
		nodo *nuevonod=crear(x,padre01);
	    arbol=nuevonod;
	    if(padre01==NULL){
	    	arbol->nivel=0;
		}
		else{
		arbol->nivel=padre01->nivel+1;	
		}
	    
	}
	else {
		
		int valorR=arbol->data;
		if(x<valorR){
			
			incertar(arbol->izquierdo,x,arbol);
		}
		else{
			
			incertar(arbol->derecho,x,arbol);
		}
	}
	
}
void mostrar(NODO arbol1, int cont){
	if(arbol1==NULL){
		return;
	}
	else{
		mostrar(arbol1->derecho,cont+1);
		for(int i=0;i<cont;i++){
			cout<<"   ";
		}
		cout<<"< "<<arbol1->data<<"<" <<arbol1->nivel<<" >"<<endl;
		
		mostrar(arbol1->izquierdo,cont+1);
	}
}
bool buscar(NODO arbol2,int B){
	if(arbol2==NULL){
		return false;
	}
	else if (arbol2->data==B){
		return true;
	}
	else if(B<arbol2->data){
		return buscar(arbol2->izquierdo,B);
	}
	else if(B>arbol2->data){
		return buscar(arbol2->derecho,B);
	}
		
		
	
}
void preorden(NODO arbol0){
	if(arbol0==NULL){
	  return;
	}
	else{
		cout<<arbol0->data<<"-";
		preorden(arbol0->izquierdo);
		preorden(arbol0->derecho);
	}
}

void inorden(NODO arbol01){
	if(arbol01==NULL){
		return;
	}
	else{
		inorden(arbol01->izquierdo);
		cout<<arbol01->data<<"-";
		inorden(arbol01->derecho);
	}
}
void postorden(NODO arbol02){
	if(arbol02==NULL){
		return;
	}
	else{
		postorden(arbol02->izquierdo);
		postorden(arbol02->derecho);
		cout<<arbol02->data<<"-";
	}
}
void eliminar(NODO X, int obx){
	if(X==NULL){
		return;
	}
	else if(obx<X->data){
		eliminar(X->izquierdo,obx);
	}
	else if(obx>X->data){
		eliminar(X->derecho,obx);
	}
    else{
    	eliminarnodo(X);
	}	
}
NODO izquierdo(NODO arbol03){
if(arbol03==NULL){
	return NULL;
}
if(arbol03->izquierdo !=NULL){
	return izquierdo(arbol03->izquierdo);
}
else{
	return arbol03;
}
	
}
void sustituir(NODO arbol04, NODO remplazar){
	if(arbol04->owl){
		if(arbol04->data==arbol04->owl->izquierdo->data){
			arbol04->owl->izquierdo=remplazar;
		}
		else if(arbol04->data==arbol04->owl->derecho->data){
			arbol04->owl->derecho=remplazar;
		}
	}
	if(remplazar){
		remplazar->owl=arbol04->owl;
	}
}
void dealte(NODO F){
	F->derecho=NULL;
	F->izquierdo=NULL;
	delete F;
}
void eliminarnodo(NODO eliminar){
	if(eliminar->derecho && eliminar->izquierdo !=NULL){
		nodo *mimino=izquierdo(eliminar->derecho);
		eliminar->data=mimino->data;
		eliminarnodo(mimino);
	}
	else if(eliminar->derecho!=NULL &&eliminar->izquierdo==NULL){
		sustituir(eliminar,eliminar->derecho);
		dealte(eliminar);
	}
	else if(eliminar->izquierdo!=NULL && eliminar->derecho==NULL){
		sustituir(eliminar,eliminar->izquierdo);
		dealte(eliminar);
	}
	else{
		sustituir(eliminar,NULL);
		dealte(eliminar);
	}
}
void niveles(NODO arbol23){
	if(arbol23==NULL){
		return;
	}
	else{
	nodoc *arr =getnodoC(arbol23->data,arbol23->nivel);
	enlazarC(arr);
    niveles(arbol23->izquierdo);
    niveles(arbol23->derecho);
	}
	
	
}
NODOC getnodoC(int xs, int niv){
	NODOC p2 = new nodoc();
	p2->dato=xs;
	p2->nivel2=niv;
	p2->siguiente=NULL;
	n_colas=n_colas+1;
	return p2;
}
NODOC getnodoC2(int xs2){
	NODOC p2 = new nodoc();
	p2->dato=xs2;
	
	p2->siguiente=NULL;
	return p2;
}
void enlazarC(NODOC alch){
	if(inicio==NULL){
		inicio=ult=alch;
	}
	else{
		ult->siguiente=alch;
		ult=alch;
	}
}
void enlazarC2(NODOC alch2){
	if(inicio2==NULL){
		inicio2=ult2=alch2;
	}
	else{
		ult2->siguiente=alch2;
		ult2=alch2;
	}
}
void imprimir(int bus){
	nodoc *xau=inicio;
	int may=-1;
	int con=0;
	int vect[n_colas];
	while(con!=n_colas){
		cout<<" el valor es "<<xau->dato<<endl;
		if(xau->nivel2>may){
			may=xau->nivel2;
		}
		xau=xau->siguiente;
		con=con+1;
	}
	
	int cont3=0;
	int k=0;
	int n=0;
	nodoc *cv = inicio;
	while(cont3<=may){
	 cv=inicio;
	 n=0;
		while(n!=n_colas){
			
			if(cv->nivel2==cont3){
				vect[k]=cv->dato;
				k=k+1;
			}
			cv=cv->siguiente;
			n=n+1;
		}
		cont3=cont3+1;	
	}
		
	int hail=bus;
	for(int h=0; h<n_colas; h++){
		cout<<vect[h]<<"-";
		if(vect[h]==hail){
			break;
		}
	}
}
void pro(int busqueda, NODO pp){
	nodo *t=pp;
	
	if(t->vistitado!=true){
		nodoc *gg=getnodoC2(t->data);
		enlazarC2(gg);
	}
	int aa=busqueda;
	t->vistitado=true;
  if(t->data==aa){
    	
	}
	else{
		if(t->izquierdo!=NULL && t->izquierdo->vistitado!=true){
			t=t->izquierdo;
			pro(aa,t);                                                      
		}
		else if(t->derecho!=NULL && t->derecho->vistitado!=true ){
			t=t->derecho;
		  pro(aa,t);
		}
		else{
			t=t->owl;
			//cuando regrese eliminar su valor
			eliminar();
			pro(aa,t);
		}
	}
}
void eliminar(){
	nodoc *aux2=inicio2;
	if(aux2->siguiente==NULL){
		aux2->dato=0;
		cout<<"ha salido el ultimo elemento"<<endl;
	}
	else{
	
	while(aux2->siguiente!=ult2){
		aux2=aux2->siguiente;
	}
	ult2=aux2;
	ult2->siguiente=NULL;
}
}
void imprimirpila(){
	nodoc *aux=inicio2;
	int cont2=0;
	do{ 
	 cout<<"el valor es "<<aux->dato<<endl;
	 aux=aux->siguiente;
	 cont2=cont2+1;
	}while(cont2!=n_pila);
}
