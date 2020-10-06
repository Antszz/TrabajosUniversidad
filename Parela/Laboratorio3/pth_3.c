#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>



#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>


int counter=0;
int thread_count=4;
pthread_mutex_t barrier_mutex;

void* threadFn(void* rank){
	long my_rank = (long) rank;
	srand(my_rank);

    pthread_mutex_lock(&barrier_mutex);
    counter++;
    pthread_mutex_unlock(&barrier_mutex);
    printf("thread %ld is waiting\n", my_rank);
    while (counter < thread_count);
    printf("thread %ld finish\n", my_rank);
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