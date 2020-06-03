//시간복잡도를 충분히 고민해보고 풀이를 시작하는것이 시간절약에 좋다.
#include <bits/stdc++.h> 
using namespace std;
 #define ONLINE_JUDGE

typedef long long ll;
typedef unsigned long long ull;

int main() {

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin) ;
    freopen("output.txt", "w", stdout) ;
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL) ; cout.tie(NULL) ;
    int n;
    cin >> n;
    vector<int> v;
    for (int i=0; i<n; i++){
        int num;
        cin >> num;
        v.push_back(num);
    }
    int idx=0;
    int cnt = 0;
    bool flag = true;
    for (int i=0; i<=n-2; i++){
        if (v[i] > v[i+1]){
            cnt++;
            if (cnt > 2){
                flag = false;
                break;
            }
            idx = i+1;
        }
        if (!flag) break;
    }
    int res;
    if (cnt == 0) res = 0;
    else if (cnt == 1){
        bool flag = true;
        for (int i=idx; i<=idx+n-2; i++){
            if (v[i%n] > v[(i+1)%n]){
                flag = false;
                break;
            }
        }
        if (!flag) res = -1;
        else res = n-idx;
    }
    else res = -1;
    cout << res << endl;
    return 0 ;
}