//문제는 잘 이해했으나, 풀이를 심사숙고하지 못했다.
//완전탐색으로 풀면되는 생각보다 쉬운문제였다.
#include <bits/stdc++.h> 
  
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
int flag[11];
int m;

bool recursion(int leftScale,int rightScale,int lastWeight,bool isLeft,vector<int>& res){
    if (res.size() == m){
        return true;
    } 
    for (int i=1; i<=10; i++){
        int diff = abs(leftScale - rightScale);
        if (flag[i] == 1 && i != lastWeight && diff < i){
                int newLeftScale = leftScale; 
                int newRightScale = rightScale;
                if (isLeft) {
                    if (leftScale + i > rightScale){
                        newLeftScale += i;
                    } else continue;
                }
                else {
                    if (rightScale + i > leftScale){
                        newRightScale += i;
                    } else continue;
                }
                res.push_back(i);
                bool isFind = recursion(newLeftScale,newRightScale,i,!isLeft,res);
                if (isFind) return true;
                res.pop_back();
            }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL) ; cout.tie(NULL) ;

    string s;
    cin >> s;
    vector<int> v;
    for (int i=0; i<s.length(); i++){
        if (s[i] == '1'){
            flag[i+1] = 1;
        }
        else{
            flag[i+1] = 0;
        }
    }
    cin >> m;
    int leftScale = 0; int rightScale = 0;
    int lastWeight = -1;
    bool isLeft = true;
    vector<int> weightList;
    bool isAnsExist = recursion(leftScale,rightScale,lastWeight,isLeft,weightList);

    if (isAnsExist){
        cout << "YES" << endl;
        cout << weightList[0];
        for (int i=1; i<weightList.size(); i++){
            cout << " " << weightList[i];
        }
        cout << endl;
    }
    else{
        cout << "NO" << endl;
    }
    return 0 ;
}