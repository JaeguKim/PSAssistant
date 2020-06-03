//항상 내 코드가 틀릴수 있다는 사실을 염두해 두자.
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,m,k;
    cin >> n >> m >> k;
    vector<pair<int,int>> cells;
    for (int i=1; i<=n; i++){
        if (i%2 == 0){
            for (int j=m; j>=1; j--){
                cells.push_back(make_pair(i,j));
            }
        }
        else {
            for (int j=1; j<=m; j++){
                cells.push_back(make_pair(i,j));
            }
        }
    }

    int curIdx = 0;
    for (int i=0; i<k-1; i++){
        cout << "2 " << cells[curIdx].first << " " << cells[curIdx].second << " " << cells[curIdx+1].first << " " << cells[curIdx+1].second << endl;
        curIdx+=2;
    }
    cout << (n*m-curIdx);
    for (int i=curIdx; i<n*m; i++){
        cout << " " << cells[i].first << " " << cells[i].second;
    }
}