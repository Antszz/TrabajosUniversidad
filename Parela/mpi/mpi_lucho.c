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
	int pong;
	while(pong<=limit){
		
		if(my_rank==2 ){
			pong = 0;
			MPI_Send(&pong,1,MPI_INT,0,0,MPI_COMM_WORLD);
			MPI_Recv(&pong,1,MPI_INT,0,0,MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			if(pong==limit){
				
				printf("Valor final %d de %d ",my_rank, limit);
			}
		
		}
		if(my_rank == 0){
			pong++;
			MPI_Send(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
			//sprintf(pinpong, "%d\n", pong);
			MPI_Recv(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			MPI_Send(&pong, 1, MPI_INT, 2, 0, MPI_COMM_WORLD);
			
		}
		else{
			MPI_Recv(&pong, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			pong++;
			MPI_Send(&pong, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
			
			
			//sprintf(pinpong, "%d\n", pong);

		}
	}
	
	MPI_Finalize();
	return 0;
}