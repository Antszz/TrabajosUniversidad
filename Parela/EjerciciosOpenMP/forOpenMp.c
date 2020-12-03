#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    omp_set_num_threads(strtol(argv[1], NULL, 10));
    int n = 5;
#pragma omp parallel
{
    printf("Hola is processed by thread %d\n", omp_get_thread_num());
#pragma omp parallel for
    for(int i=0; i<n; i++){
        printf("Iterion %d is processed by thread %d\n", i, omp_get_thread_num());
    }
#pragma omp master
    printf("Mater is processed by thread %d\n", omp_get_thread_num());
}
}