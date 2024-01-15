
#include <stdio.h>
#include <stdlib.h>
typedef struct _TMatriz_{
    float ** conteudo;
    int linhas;
    int colunas;
    } TMatriz;

typedef enum _button_ {ON, OFF} Button;
typedef struct _house_ {char * address;} House;

void criar (TMatriz *matriz, int l, int c){
    int i, j;
    matriz->conteudo = (float **)malloc(sizeof(float*[l]));
    for(i=0; i<l; i++){
        matriz->conteudo[i] = (float *)malloc(sizeof(float[c]));
    }
    matriz->linhas = l;
    matriz->colunas = c;
}
void setarValor(TMatriz *matriz, int i, int j, float valor){
    matriz->conteudo[i][j] = valor;

}
float obterValor(TMatriz matriz, int i, int j){
    return(matriz.conteudo[i][j]);
}

void destruir (TMatriz *matriz){
    int i;
    for(i=0; i<matriz->linhas; i++){
        free(matriz->conteudo[i]);
    }
    free(matriz->conteudo);
    matriz->linhas= 0;
    matriz->colunas=0;
}

int main()
{
    int i, j, l, c;
    float valor;
    TMatriz matriz;
    printf("MANIPULACAO DE MATRIZ DE NUMEROS...\n");
    printf("NUMERO DE LINHAS DA MATRIZ: ");
    scanf("%d", &l);
    printf("NUMERO DE COLUNAS DA MATRIZ: ");
    scanf("%d", &c);
    // Fun��o cria: aloca espa�o em mem�ria para o conte�do de uma matriz de l linhas e c colunas.
    // Essa fun��o tamb�m estabelece os valores para a quantidade de linhas e
    // a quantidade de colunas do tipo TMatriz.
    criar(&matriz, l, c);
    for (i=0; i<matriz.linhas; i++){
        for (j=0; j<matriz.colunas; j++){
            printf("M[%d][%d] = ", i, j);
            scanf("%f", &valor);
            // Fun��o setarValor: armazena o valor na posi��o da linha i
            // e coluna j da vari�vel do tipo TMatriz.
            setarValor(&matriz, i, j, valor);
        }
    }

    for (i = 0; i < matriz.linhas; i++){
        for (j = 0; j < matriz.colunas; j++){
            // Fun��o obterValor: retorna o valor obtido na posi��o correspondente � linha i
            // e coluna j da vari�vel do tipo TMatriz.
            printf("%10f ", obterValor(matriz, i, j));
            printf("\n");
        }
    }
    // Fun��o destr�i: libera o espa�o alocado para a vari�vel do tipo TMatriz e atribui o valor zero
    // para as quantidades de linha e de coluna para a vari�vel do tipo TMatriz.
    destruir(&matriz);
    return 0;
}
