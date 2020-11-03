#include <iostream>
#include "LargeIntegers.cpp"
#include <math.h>
#include <vector>

using namespace std;

InfInt exp_rapida(InfInt base, InfInt exponente, InfInt modulo){
	InfInt x(1);
	InfInt y(base % modulo);
	InfInt b(exponente);
	InfInt i(0);
	InfInt par(2);
	InfInt impar(1);
	while(b > i){
		if((b % par) == i){
			y = (y*y) % modulo;
			b = b / par;
		}
		else{
			x = (x*y) % modulo;
			b = b - impar;
		}
	}
	return x;
}

InfInt log_lento(InfInt base_log, InfInt logaritmo, InfInt modulo){
	cout<<logaritmo.logar(base_log)<<endl;
	return (logaritmo.logar(base_log)) % modulo;
}

vector<InfInt> diffie_hellman(InfInt p, InfInt alpha, InfInt Xa, InfInt Xb){
	InfInt Ya, Yb, Ka, Kb;

	Ya = exp_rapida(alpha, Xa, p);
	Yb = exp_rapida(alpha, Xb, p);

	cout<<Ya<<" "<<Yb<<endl;

	Ka = exp_rapida(Yb, Xa, p);
	Kb = exp_rapida(Ya, Xb, p);

	vector<InfInt> v = {Ka, Kb};

	return v;
}


vector<InfInt> diffie_hellman_reverse(InfInt p, InfInt alpha, InfInt Ya, InfInt Yb){
	InfInt Xa, Xb, Kb, Ka;

	Xa = log_lento(alpha, Yb, p);
	Xb = log_lento(alpha, Ya, p);

	vector<InfInt> v = {Xa, Xb};

	return v;

}

int main(){
	vector<InfInt> v;

	InfInt p("5"), alpha("3"), Xa("9"), Xb("27");

	v = diffie_hellman(p, alpha, Xa, Xb);
	cout<<v[0]<<" "<<v[1]<<endl;

	vector<InfInt> vR;
	InfInt Ya("3"), Yb("2");
	vR = diffie_hellman_reverse(p, alpha, Ya, Yb);
	cout<<vR[0]<<" "<<vR[1]<<endl;

	return 0;
}
