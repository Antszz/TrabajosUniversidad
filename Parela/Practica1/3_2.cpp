#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define max 300

int main(){
	
	clock_t t;

	int f,c,z;
	int A[max][max];
	int B[max][max];
	int C[max][max];


	for(int i=0;i<max;i++){
		for(int j=0;j<max;j++){
			A[i][j]=rand()%max;
			B[i][j]=rand()%max;
			C[i][j]=0;
		}	
	}

	int block_size=150;

	t=clock();

	for (int i = 0; i < max; i += block_size)
		for (int j = 0; j < max; j += block_size)
			for (int k = 0; k < max; k += block_size)
				for (int ii = i; ii < min(i + block_size, max); ++ii)
					for (int jj = j; jj < min(j + block_size, max); ++jj)
						for (int kk = k; kk < min(k + block_size, max); ++kk)
							C[ii][jj] += A[ii][kk] * B[kk][jj];
	t = clock() - t;

    cout<<"Para un valor maximo de "<<max<<endl;
    printf ("La multiplicacion demoró %ld clicks (%f segundos).\n",t,((float)t)/CLOCKS_PER_SEC);


}