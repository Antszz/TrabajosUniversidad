#include <bits/stdc++.h>
using namespace std;
#define MAX 300

int main(){

	clock_t t;

	int f,c,z;
	int A[MAX][MAX];
	int B[MAX][MAX];
	int C[MAX][MAX];


	for(int i=0;i<MAX;i++){
		for(int j=0;j<MAX;j++){
			A[i][j]=rand()%MAX;
			B[i][j]=rand()%MAX;
			C[i][j]=0;
		}	
	}

	int block_size=150;

	t=clock();

	for (int k = 0; k < MAX; k += block_size)
		for (int j = 0; j < MAX; j += block_size)
			for (int i = 0; i < MAX; ++i)
				for (int jj = j; jj < min(j + block_size, MAX); ++jj)
					for (int kk = k; kk < min(k + block_size, MAX); ++kk)
						C[i][jj] += A[i][kk] * B[kk][jj];

	t = clock() - t;

    cout<<"Para un valor maximo de "<<MAX<<endl;
    printf ("La multiplicacion demoró %ld clicks (%f segundos).\n",t,((float)t)/CLOCKS_PER_SEC);

    return 0;
}