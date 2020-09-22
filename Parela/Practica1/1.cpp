#include <bits/stdc++.h>

using namespace std;

#define max 600

int main(){

	clock_t t;

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

	t = clock();

	for (int i = 0; i < max; ++i)
	{
		for (int j = 0; j < max; ++j)
		{
			y[i] += A[i][j]*x[j];
		}
	}
	t = clock() - t;

    printf ("Primer bucle anidado demoró %ld clicks (%f segundos).\n",t,((float)t)/CLOCKS_PER_SEC);


	//Assign y = 0
	for (int i = 0; i < max; ++i)
	{
		y[i]=0;
	}

	t = clock();

	for (int j = 0; j < max; ++j)
	{
		for (int i = 0; i < max; ++i)
		{
			y[i] += A[i][j]*x[j];
		}
	}
	t = clock() - t;

    printf ("Segundo bucle anidado demoró %ld clicks (%f segundos).\n",t,((float)t)/CLOCKS_PER_SEC);

	return 0;
}