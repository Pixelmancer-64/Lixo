#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int ladoDoTriangulo (float lado1, float lado2, float lado3)
{
    int triangulo;

    if (lado1<=0 || lado2<=0 || lado3<=0)
    {
            return triangulo= 0;
     } else 
    return triangulo=1;
}
int qualTriangulo (float lado1, float lado2, float lado3)
{
    int triangulo, resposta;
    resposta=ladoDoTriangulo(lado1, lado2, lado3);
    if (resposta==0){
        return triangulo=0;
    }
    else {
        return triangulo=1;
    }
   
     if (lado1==lado2 || lado2==lado3 || lado3==lado1)
     {
      return triangulo=2;
     }
     else if (lado1==lado2 && lado1==lado3 && lado2==lado3)
     {
        return triangulo=3;
     }
       
}
main()
{
    float num1, num2, num3;
    int resultado;
    printf("Digite o valor do primeiro lado do triangulo: ");
    scanf("%f", &num1);
    printf("Digite o valor do segundo lado do triangulo:\n ");
    scanf("%f", &num2);
    printf("Digite o valor do terceiro lado do triangulo:\n ");
    scanf("%f", &num3); 

    resultado= qualTriangulo(num1, num2, num3);
   if (resultado==1){
   printf("O triangulo é Escaleno \n");}
   else if (resultado==2){
    printf("O triangulo é Isosceles \n");
   }
   else if (resultado==3){
    printf("O triangulo é Equilatero \n");
   }
   else {
    printf("Não é um triangulo \n");}

    getchar();

}