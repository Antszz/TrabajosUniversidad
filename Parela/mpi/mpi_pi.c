#include <stdio.h>
#include <string.h>
#include <mpi.h>
#include <stdlib.h>

double calPI(int inic, int finC){
	double factor = 1.0;
	double sum = 0.0;
	if(inic % 2 != 0)
		factor = -1.0;

	for (int i = inic; i < finC; ++i)
	{
		sum += factor/(2*i+1);
		factor *= -1;
	}
	return sum;
}

int main(){
	int comm_sz;
	int my_rank;
	FILE *fp;

	MPI_Init(NULL, NULL);
	MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

	char str_rank[15];
	char str_ubicacion[15];
	char str_pong[15];
	strcpy(str_ubicacion, "../pasosPong");
	sprintf(str_rank, "%d.txt", my_rank);
	strcat(str_ubicacion, str_rank);
	fp = fopen(str_ubicacion, "a+t");

	int* tiros;

	if(my_rank == 0){
		printf("Colocar numero de tiros\n");
		scanf("%d", tiros);
	}
	MPI_Bcast(tiros, 1, MPI_INT, 0, MPI_COMM_WORLD);

	int inicioC, finC;
	int salto = *tiros/comm_sz;
	if(my_rank == 0){
		inicioC = 0;
		finC = salto;
		//printf("salto %d\n", tiros);
	}
	else if(my_rank == comm_sz - 1){
		inicioC = my_rank*salto;
		finC = *tiros;
	}
	else{
		inicioC = my_rank*salto;
		finC = inicioC + salto;
	}

	double totalSum;
	double localSum = calPI(inicioC, finC);

	sprintf(str_pong, "%d\n", finC);
	fputs(str_pong,fp);

	MPI_Reduce(&localSum, &totalSum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

	if( my_rank == 0){
		printf("El valor calculado de PI es %f\n", localSum);
	}
	/*

	int pong = 0;
	fp = fopen(str_ubicacion, "a+t");
	while(pong<limit){
		if(my_rank == 0){
			pong++;
			MPI_Send(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
			sprintf(str_pong, "%d\n", pong);
			fputs(str_pong,fp);
			MPI_Recv(&pong, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		}
		else{
			MPI_Recv(&pong, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
			pong++;
			MPI_Send(&pong, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
			sprintf(str_pong, "%d\n", pong);
			fputs(str_pong,fp);
		}
	}
	*/
	fclose(fp);


	MPI_Finalize();
	return 0;
}
