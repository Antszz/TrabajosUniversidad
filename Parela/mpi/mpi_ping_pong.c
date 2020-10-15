#include <stdio.h>
#include <string.h>
#include <mpi.h>
#include <stdlib.h>

int main(){
	int comm_sz;
	int my_rank;

	MPI_Init(NULL, NULL);
	MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
	int limit = 20;	

	int pong = 0;
	if(my_rank==2){
			pong++;
			MPI_Send(&pong, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);}
	if(my_rank==0){
			MPI_Recv(&pong, 1, MPI_INT, 2, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			pong++;
			MPI_Send(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
		}
	if(my_rank != 2){
		while(1){
			if(my_rank == 1){
				MPI_Recv(&pong, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
				pong++;
				MPI_Send(&pong, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
				if(pong>limit){
					MPI_Send(&pong, 1, MPI_INT, 2, 0, MPI_COMM_WORLD);
					break;
				}
			}
			else{
				MPI_Recv(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
				pong++;
				MPI_Send(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
				if(pong>limit){
					break;
				}
			}
		}

	}
	if(my_rank==2){
		MPI_Recv(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		printf("Soy el hilo %d y el resultado es %d\n", my_rank, pong);
	}
	MPI_Finalize();
	return 0;
}
