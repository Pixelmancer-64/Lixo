#include <stdlib.h>
#include <stdio.h>

int main()
{
    int **array;

    int row;
    int column;
    int i, j;

    printf("me fala ai o numero de fileiras:");
    scanf("%d", &row);

    printf("me fala ai o numero de colunas:");
    scanf("%d", &column);


    array = (int **)malloc(sizeof(int *) * row);
    for (i = 0; i < row; i++)
    {
        array[i] = (int *)malloc(sizeof(int) * column);
    }

    for (i = 0; i < row; i++)
    {
        for (j = 0; j < column; j++)
        {
            printf("coord array[%d][%d]", i, j);
            scanf("%d", &array[i][j]);
        }
    }

    printf("resultado:\n\n\n");

    for (i = 0; i < row; i++)
    {
        for (j = 0; j < column; j++)
        {
            printf("Valor array[%d][%d] = %d\n", i, j, array[i][j]);
        }
    }

    for(i=0; i<row; i++){
        free(array[i]);
    }
    free(array);
}