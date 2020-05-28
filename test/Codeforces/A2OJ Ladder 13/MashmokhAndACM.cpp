//#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
using namespace std;
typedef long long ll;
ll dp[2010][2010];
const ll mod = pow(10,9)+7;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n,k;
    cin >> n >> k;
    for (int i=1; i<=n; i++){
        dp[1][i] = 1;
    }
    for (int i=2; i<=k; i++){
        for (int j=1; j<=n; j++){
            for (int z=j; z<=n; z+=j){
                dp[i][z] += dp[i-1][j]%mod;
            }
        }
    }
    ll res = 0;
    for (int i=1; i<n+1; i++){
        res += dp[k][i]%mod;
    }
    res %= mod;
    cout << res;
}