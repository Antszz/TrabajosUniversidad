#include <bits/stdc++.h>

using namespace std;

#define max 500

int main(){

	clock_t t;

//Multiplicacion de matrices clásica con 3 bluces anidados
    int a[max][max];
	int b[max][max];
	int c[max][max];

	for (int i = 0; i < max; ++i)
	{
		for (int j = 0; j < max; ++j)
		{
			a[i][j] = rand()%max;
			b[i][j] = rand()%max;
		}
	}

	t=clock();
	for(int i=0; i<max; ++i)
    	for(int j=0; j<max; ++j)
      		for(int z=0; z<max; ++z)
        		c[i][j] += a[i][z] * b[z][j];
    t = clock() - t;

    cout<<"Para un valor maximo de "<<max<<endl;
    printf ("La multiplicacion demoró %ld clicks (%f segundos).\n",t,((float)t)/CLOCKS_PER_SEC);


	return 0;
}