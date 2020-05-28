#include <bits/stdc++.h>
using namespace std;
int main(){
    int t = 0;
    cin >> t;
    for (int i=0;i<t;i++){
        long long a,b,c,d;
        cin >> a >> b >> c >> d;
        long long res = 0;
        if (a<=b)
            res = b;
        else{
            if (c-d<0)
                res = -1;
            else{
                int x = ceilf(float(a-b)/float(c-d));
                res = b+c*x;
            }
        }
        cout << res << endl;
    }
}