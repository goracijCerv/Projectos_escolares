/*
Universidad Autonoma de Aguascalientes
Centro de Ciencias Básicas
Departamento de Ciencias de la Computación
Materia: optimisacion
Alumno:
J.Horacio Cervantes.P
Profesora: Dr.
*/
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<stdbool.h>
int main(){
	double es=5;
	bool bandera=false;
	int it=0;
	double x0,x1,x2,x3,x3sup,x3inf,fx0,fx1,fx2,fx3,ea;
	printf("Incerte el valor de x0: ");
	scanf("%lf",&x0);
	printf("\nIncerte el valor de x1: ");
	scanf("%lf",&x1);
	printf("\nIncerte el valor de x2: ");
	scanf("%lf",&x2);
	printf("\n");
	printf("EL valor de es tomado es: 1%\n");
	do{
		fx0=(2*pow(x0,2)) + (16/x0);//(2*sin(x0))-(pow(x0,2)/2);
		fx1=(2*pow(x1,2)) + (16/x1);//(2*sin(x1))-(pow(x1,2)/2);
		fx2=(2*pow(x2,2)) + (16/x2);//(2*sin(x2))-(pow(x2,2)/2);
		x3sup=((fx0*(pow(x1,2)-pow(x2,2)))+(fx1*(pow(x2,2)-pow(x0,2)))+(fx2*(pow(x0,2)-pow(x1,2))));
		x3inf=((2*fx0*(x1-x2))+(2*fx1*(x2-x0))+(2*fx2*(x0-x1))); 
		x3=x3sup/x3inf;
		fx3=(2*pow(x3,2))+(16/x3);//((2*sin(x3))-(pow(x3,2)/2));
		if(it>0){
			ea=(fabs((x3-x1)/x3))*100;
		}else{
			ea=100;
		}
		
		if(x3>x0 && x3<x1){
			x2=x1;
			x1=x3;
		}else if(x3>x1 && x3<x2){
			x0=x1;
			x1=x3;
		}else{
			bandera=true;
			printf("Ocurio un error el cual no se que signifique, yo considero que esto significa que encontramos lo mejor :)\n");
			
		}
		it++;
		printf("Ineracion: %d\n",it);
		printf("valor de x optimo: %.6lf\n",x3);
		printf("valor de la funcion evaluada en la x optima: %.6lf\n",fx3);
		printf("El error calculado en esta interacion es de: %.6lf\n",ea);
	}while(ea>es && it<10 && bandera==false);
	//Comprobar paso a paso en execel xd
	system("pause");
	return 0;
}
