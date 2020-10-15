#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>

double total_int;

double f(double x){
	return x*x;
}

double Trap(
	double left_endpt,
	double right_endpt,
	int trap_count,
	double base_len)
{
	double estimate,x;
	int i;
	estimate = (f(left_endpt) + f(right_endpt))/2.0;
	for(i = 1; i<=trap_count-1; i++){
		x = left_endpt + i*base_len;
		estimate += f(x);
	}
	estimate = estimate*base_len;
	return estimate;
}


const int MAX = 1000;

int thread_count;
sem_t* sems;

void *Trapecio(void* rank);


int main(int argc, char* argv[]) {
	long thread;
	pthread_t* thread_handles; 

	thread_count = atoi(argv[1]);

	thread_handles = (pthread_t*) malloc (thread_count*sizeof(pthread_t));
	sems = (sem_t*) malloc(thread_count*sizeof(sem_t));

	sem_init(&sems[0], 0, 1);
	for (thread = 1; thread < thread_count; thread++)
		sem_init(&sems[thread], 0, 0);

	for (thread = 0; thread < thread_count; thread++)
		pthread_create(&thread_handles[thread], (pthread_attr_t*) NULL,Trapecio, (void*) thread);

	for (thread = 0; thread < thread_count; thread++) {
		pthread_join(thread_handles[thread], NULL);
	}

	for (thread=0; thread < thread_count; thread++)
		sem_destroy(&sems[thread]);

	printf("El area es %e\n", total_int);
	free(sems);
	free(thread_handles);
	return 0;
}


void *Trapecio(void* rank) {
	long my_rank = (long) rank;
	int next = (my_rank + 1) % thread_count;
	int n = 1024, local_n;
	double a = 0.0, b = 3.0, h, local_a, local_b;
	double local_int;

   	h = (b-a)/n;
	local_n = n/thread_count;

	local_a = a + my_rank*local_n*h;
	local_b = local_a + local_n*h;
	local_int = Trap(local_a, local_b, local_n, h);

	sem_wait(&sems[my_rank]);
	total_int += local_int;
	sem_post(&sems[next]);
	return NULL;
}