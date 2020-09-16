#include <bits/stdc++.h>

using namespace std;

#define max 1000

int multiMatrices(int a[][max], int b[max][], int f, int c, int k){
	int c[max][max];
	for(int i=0; i<f; ++i)
    for(int j=0; j<c; ++j)
      for(int z=0; z<k; ++z)
        c[i][j] += A[i][z] * B[z][j];
  return c;
}

int main(){
	int a[2][3] = {{1,0,1},{0,1,2}};
	int b[3][2] = {{3,5},{-1,0},{2,-1}};
	int c[max][max];

	c = multiMatrices(a, b, 3,3,2);






	double A[max][max], x[max], y[max];

	for (int i = 0; i < max; ++i)
	{
		for (int j = 0; j < max; ++j)
		{
			A[i][j]=rand()%1000;
		}
		x[i]=rand()%1000;
		y[i]=0;
	}

	for (int i = 0; i < max; ++i)
	{
		for (int j = 0; j < max; ++j)
		{
			y[i] += A[i][j]*x[j];
		}
	}

	for (int j = 0; j < max; ++j)
	{
		for (int i = 0; i < max; ++i)
		{
			y[i] += A[i][j]*x[j];
		}
	}

	

	return 0;
}