//뭔가 손에 잡힐듯 안잡힐듯 하는 풀이다. 결국 이해는 어느정도 했으나 완전히 손에 잡히지는 않는것같다.
#include <bits/stdc++.h> 
using namespace std;
typedef unsigned long long ull;
int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL) ; cout.tie(NULL) ;

    int n,m,k;
    cin >> n >> m >> k;
    vector<ull> s(n+1);
    vector<vector<ull>> dp(n+1,vector<ull>(k+1));
    for (int i=1; i<=n; i++) cin >> s[i];
    for (int i=1; i<=n; i++) s[i] += s[i-1];
    for (int i=m; i<=n; i++){
        for (int j=1; j<=k; j++){
            dp[i][j] = max(dp[i-1][j], dp[i-m][j-1]+s[i]-s[i-m]);
        }
    }
    cout << dp[n][k] << endl;
    return 0 ;

}