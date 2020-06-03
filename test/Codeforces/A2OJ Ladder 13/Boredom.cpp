//자료형 범위 overflow에 유의한다.
#include <bits/stdc++.h>

using namespace std;

const int maxn = 100001;
long long f[maxn];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    map<int,int> hash;
    vector<pair<int,int>> vec;

    for (int i=0;i<n;i++){
        int no = 0;
        cin >> no;
        hash[no]++;
    }

    map<int,int> :: iterator it;
    for (it=hash.begin(); it!=hash.end(); it++){
        vec.push_back(make_pair(it->first,it->second));
    }

    for (int i=0; i<vec.size();i++){
        int pr = i-1;
        while (pr >= 0 && vec[pr].first+1 == vec[i].first) pr--;
        if (pr == -1) f[i] = 1LL*vec[i].first * 1LL*vec[i].second;
        else f[i] = f[pr] + 1LL*vec[i].first*1LL*vec[i].second;
        if (i != 0)
            f[i] = max(f[i],f[i-1]);
    }

    cout << f[vec.size()-1] << endl;
}