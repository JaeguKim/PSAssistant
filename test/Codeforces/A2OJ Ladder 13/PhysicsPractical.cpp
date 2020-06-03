//생각보다 간단한 문제였고, 문제를 너무 복잡학게 해석했던것같다.
#include <bits/stdc++.h> 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;

int main() {
    freopen("input.txt", "r", stdin) ;
    freopen("output.txt", "w", stdout) ;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL) ; cout.tie(NULL) ;
    int n;
    cin >> n;
    int count[5001] = {0};
    vector<int> v;
    for (int i=0;i<n;i++){
        int num;
        cin >> num;
        v.push_back(num);
        count[num]++;
    } 
    sort(v.begin(),v.end());
    int minVal = n;
    int frontSum = 0;
    int rearSum = 0;
    for (int i=1;i<=5000;i++){
        rearSum = 0;
        for (int j=i+1;j<=5000;j++){
            if (count[j] != 0 && j > 2*i){
                rearSum += count[j];
            }
        }
        int total= frontSum+rearSum;
        minVal = min(total,minVal);
        frontSum += count[i];
    }
    cout << minVal << endl;
    return 0 ;

}