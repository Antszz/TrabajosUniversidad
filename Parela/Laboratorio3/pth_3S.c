#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>



#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>


int counter=0;
int thread_count;
pthread_mutex_t barrier_mutex;
sem_t count_sem;
sem_t barrier_sem;


void* threadFn(void* rank){
	long my_rank = (long) rank;
	srand(my_rank);

    printf("thread %ld is waiting\n", my_rank);
    sem_wait(&count_sem);
    if (counter == thread_count-1) {
        counter = 0;
        sem_post(&count_sem);
        for (int j = 0; j < thread_count-1; j++)
            sem_post(&barrier_sem);
    } else {
        counter++;
        sem_post(&count_sem);
        sem_wait(&barrier_sem);
    }
    printf("thread %ld: Ejecutando!\n", my_rank);
    return NULL;
}


int main(int argc, char* argv[]) {
    long thread;
    pthread_t* thread_handles;

    thread_count = strtol(argv[1], NULL, 10);

	thread_handles = malloc (thread_count * sizeof(pthread_t));

    for (thread=0; thread < thread_count; thread++) {
        pthread_create(&thread_handles[thread], NULL, threadFn, (void*) thread);
    }
    for (thread=0; thread < thread_count; thread++) {
        pthread_join(thread_handles[thread], NULL);
    }

    return 0;
}