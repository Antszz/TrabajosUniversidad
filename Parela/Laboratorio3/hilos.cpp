#include <pthread.h>
#include <iostream>
#include <cstdlib>
//#include <bits/stdc++.h>
using namespace std;
#define NUM_TH 6
int buffer[NUM_TH/2]={0};
void*Rutina2(void * threadid){
    long tid;
    tid=(long)threadid;
   // cout<<"Hola mundo! thread ID,"<<tid<<endl;
    for(int i=0;i<10;i++){
        cout<<"Hilo:"+to_string(tid)+"*"+to_string(i)+"\n";
    }
    pthread_exit(NULL);
}
void*PrintHello(void * threadid){
    long tid;
    tid=(long)threadid;
    cout<<"Hola mundo! thread ID,"+to_string(tid)+"\n";

    pthread_exit(NULL);
}
void*Producir(void * threadid){
    long tid;
    tid=(long)threadid;
    cout<<"PRODUCIENDO ESPACIO:"+to_string(tid)+"\n";
    buffer[tid]=1;
    pthread_exit(NULL);
}
void*Consumir(void * threadid){
    long tid;
    tid=(long)threadid;
    while(buffer[tid]==0){
        cout<<"ESPERANDO ESPACIO:"+to_string(tid)+"\n";
    }
    cout<<"CONSUMIENDO ESPACIO:"+to_string(tid)+"\n";
    buffer[tid]=0;

    pthread_exit(NULL);
}
int main(){
    pthread_t threads[NUM_TH];
    int rc;
    int i;
    for(i=0;i<NUM_TH/2;i++){
        cout<<"main():creating thread,"+to_string(i)+"\n";
        rc=pthread_create(&threads[i],NULL,Consumir,(void*)i);

        if(rc){
            cout<<"Error creating thread,"<<rc<<endl;
            exit(-1);
        }
    }

    for(int i=0;i<100000;i++){}
    for(i=0;i<NUM_TH/2;i++){
        cout<<"main():creating thread,"+to_string(i)+"\n";
        rc=pthread_create(&threads[i],NULL,Producir,(void*)i);

        if(rc){
            cout<<"Error creating thread,"<<rc<<endl;
            exit(-1);
        }
    }

    pthread_exit(NULL);


}
