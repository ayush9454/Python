#include<iostream>
using namespace std;
int main(){
    int a;
    cin>>a;
    for(int i=0; i<a; i++){
        for(int j=0; j<i; j++){
            for(int l=0; l<j; j++){
                cout<<"*";
            }
        }
    cout<<endl;
    }
}