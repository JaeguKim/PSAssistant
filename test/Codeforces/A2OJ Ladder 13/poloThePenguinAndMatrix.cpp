#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n,m,d;
    cin >> n >> m >> d;
    vector<int> vec;
    for (int i=0; i<n; i++){
        for (int j=0;j<m;j++){
            int num = 0;
            cin >> num;
            vec.push_back(num);
        }
    }
    int res = INT_MAX;
    for (int i=0; i<vec.size(); i++){
        int cnt = 0;
        for (int j=0; j<vec.size();j++){
            if (abs(vec[j]-vec[i])%d != 0){
                cout << "-1" << endl;
                return 0;
            }
            cnt+=abs(vec[j]-vec[i])/d;
        }
        res = min(res,cnt);
    }
    cout << res << endl;
}