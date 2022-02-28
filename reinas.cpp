 // implementacion de la forma de solucionar el problema de las n reinas
 // J.Horacio Cervantes P
 #include <sys/time.h>
 #include<bits/stdc++.h>
 #define n 8 
 using namespace std;
 int contsol=0;
 int contposi=0;
struct timeval stop, start;
 void imprimirtab(bool tab[n][n]){
 	 gettimeofday(&stop, NULL);
 	 contsol++;
 	 cout<<"Solucion "<<contsol<<endl;
 	 for(int i=0; i<n; i++){
 	 	  for(int j=0; j<n; j++){
 	 	  	 cout<<" "<<tab[i][j]<<" ";
				}
				cout<<endl;
		}
	//printf("tomo %lu milesegundos\n", (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);
	cout<<"El tiempo tomado para la solucion fue de "<<(stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec<<" milesegundos"<<endl; 
	cout<<endl;	
 }
 bool tabien(bool tab[n][n],int fil,int col){
 	 //verificando la columna parte superior.
 	 int i2,j2;
 	 for(int i2=fil; i2>=0; i2--){
 	 	  if(tab[i2][col]==true){
 	 	  	return false;
			}
		}
		/*verificando columna parte inferior
		for(int i3=fil; i3<n; i3++){
			if(tab[i3][col]==true){
				return false;
			}
		}
		*/
		//verificar fila parte derecha
		for(j2=col;j2<n;j2++){
			if(tab[fil][j2]==true){
				return false;
			}
		}
		//verificar fila parte izquierda
		for(j2=col:j2>=0;j2--){
			if(tam[fil][j2]==true){
				return false;
			}
		}
		// verificando diagolan izquierda superior
		for( i2=fil,j2=col; i2>=0 && j2>=0; i2--,j2--){
			if(tab[i2][j2]==true){
				return false;
			}
		}
		
		//verificando diagonal izquierda inferior
	 for(i2=fil, j2=col; i2<n && j2>=0; i2++,j2--){
	 	if(tab[i2][j2]==true){
	 		return false;
		 }
	 }
	 
	 // verificando diagonal dercha superior
	 for(i2=fil,j2=col; i2>=0 && j2<n; i2--,j2++){
	 	if(tab[i2][j2]==true){
	 		return false;
		 }
	 }
	 
	 //verificando diagogal derecha inferior
	 for(i2=fil,j2=col; i2<n && j2<n; i2++,j2++){
	 	if(tab[i2][j2]==true){
	 		return false;
		 }
	 }
	 
	 return true;
 }
 void resolver(bool tab[n][n], int fila){
 	 if(fila==n){
 	     
 	 	 imprimirtab(tab);
		}
		for(int col=0; col<n; col++){
			if(tabien(tab,fila,col)==true){
				tab[fila][col]=true;
				contposi++;
				resolver(tab,fila+1);
			}
			tab[fila][col]=false;			
		}
 }

 int main(){
    bool tablero[n][n];
    for(int o=0; o<8; o++){
        for(int o2=0; o2<8; o2++){
         tablero[o][o2]=false;   
            
        }
    }
    gettimeofday(&start, NULL);
    resolver(tablero,0);
    system("pause");
    return 0;
 }
