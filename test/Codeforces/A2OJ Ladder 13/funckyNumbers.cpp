//완전제곱식에 대한 지삭으로 쉽게 풀이가능
//정수 범위 long long 으로 증가
#include <bits/stdc++.h> 
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL) ; cout.tie(NULL) ;

    ll n,n1,n2,mult = 0;
    cin >> n;

    for (ll k1=1;k1<sqrt(n);k1++){
        ll k2 = (-1+sqrt(1-4*k1*(k1+1)+8*n))/2;
        if (k1*(k1+1) + k2*(k2+1) == 2*n){
            cout << "YES" << endl;
            return 0;
        }
    }
    cout << "NO" << endl;
}