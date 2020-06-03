#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ull;
int main(){
    int n;
    ull MAX = pow(10,18);
    cin >> n;
    ull res = 1;
    for (int i=0;i<n;i++){
        ull num = 0;
        cin >> num;
        res*=num;

    }
    if (res>MAX){
    cout << "-1";
    }
    else
        cout << res<<endl;
}