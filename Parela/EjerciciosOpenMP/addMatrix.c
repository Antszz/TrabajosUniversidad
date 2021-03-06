#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
	float A[16][16];
	float B[16][16];
	float C[16][16];
	for (int i = 0; i < 16; ++i) {
		for (int j = 0; j < 16; ++j) {
			A[i][j] = 2;
			B[i][j] = 3;
		}
	}
    omp_set_num_threads(strtol(argv[1], NULL, 10));
#pragma omp parallel
	{
		int id = omp_get_thread_num();
		int nt = omp_get_num_threads();
        printf("Hola desde %d de un total de %d\n", id, nt);
		int size = (int) 16 / nt;
		int ini = id * size;
		int fin = ini + size;
		for (int i = ini; i < fin; ++i) {
			for (int j = 0; j < 16; ++j) {
				C[i][j] = A[i][j] + B[i][j];
                printf("A[%d][%d] = %f \n", i, j, A[i][j]);
                printf("B[%d][%d] = %f \n", i, j, B[i][j]);
			}
		}
	}

	for (int i = 0; i < 16; ++i) {
		for (int j = 0; j < 16; ++j) {
			printf("C[%d][%d] = %f \n", i, j, C[i][j]);
		}
	}

	return 0;
}