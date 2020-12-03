#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

#define maxim 100
int main(int argc, char *argv[]) {
    //omp_set_num_threads(strtol(argv[1], NULL, 10));
    int n = 10;
    int i, j;
    int A[maxim][maxim];
    A[2][1]=3;
    A[1][3]=5;
#pragma omp parallel 
    for (i = 2; i < n; i++)
    	for (j = 2; j < n; j++)
	        A[i][j] = A[i][j-1] + A[i-1][j+1];


    for (i = 0; i < n; i++){
    	for (j = 0; j < n; j++)
	        printf("%d ", A[i][j]);
        printf("\n");
    }
}