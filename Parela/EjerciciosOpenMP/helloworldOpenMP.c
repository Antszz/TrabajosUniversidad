#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
    printf("\nFuera de paralela\n");
    omp_set_num_threads(strtol(argv[1], NULL, 10));
#pragma omp parallel
    {
        int id = omp_get_thread_num();
        int nt = omp_get_num_threads();
        printf("Hola desde %d de un total de %d\n", id, nt);
    }
    printf("\n02 Fuera de paralela\n");
    return 0;
}