#include "LargeIntegers.cpp"
#include <iostream>

using namespace std;

int main(){
	
	InfInt a(256);
	InfInt b(4);
	InfInt c;

	c = a.logar(b);
	cout<<c<<endl;

	return 0;
}


