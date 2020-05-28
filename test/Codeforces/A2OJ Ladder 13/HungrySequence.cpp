#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define SIZE 10000001
int main(){
    int n;
    cin >> n;
    int cnt = 0;
   int check[SIZE] = {0};
    for (int i=2; i<=SIZE-1;i++){
        if (check[i]==0){
            cout << i << " ";
            cnt+=1;
            if (cnt==n){
                break;
            }
            for (int j=1; j*i<=SIZE;j++){
                check[j*i]=1;
            }
        }
    }
}