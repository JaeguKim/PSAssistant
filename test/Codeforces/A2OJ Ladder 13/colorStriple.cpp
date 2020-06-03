#include <iostream>
#include <vector>
using namespace std;

vector<char> vec;

char getDiffCh(vector<char> oldChs){
    for (int i=0; i< vec.size(); i++){
        bool isSame = false;
        for (int j=0; j<oldChs.size();j++)
        {
            if (vec[i] == oldChs[j]){
                isSame = true;
            }
        }
        if (isSame == false){
            return vec[i];
        }
    }
    return 'e';
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,k;
    string s;
    cin >> n >> k >> s;
    for (int i=0; i<k; i++){
        vec.push_back(char('A'+i));
    }
    char case1[2] = {'A','B'};
    char case2[2] = {'B','A'};
    if (k==2){
        int no_diff_caseA = 0;
        int no_diff_caseB = 0;
        for (int i=0; i<s.length(); i++)
        {
            if (s[i] != case1[i%2])
                no_diff_caseA += 1;
            if (s[i] != case2[i%2])
                no_diff_caseB += 1;
        }
        string ans = "";
        if (no_diff_caseA < no_diff_caseB)
        {
            cout << no_diff_caseA << endl;
            for (int i=0; i<s.length(); i++)
            {
                ans+=case1[i%2];
            }
        }
        else
        {
            cout << no_diff_caseB << endl;
            for (int i=0; i<s.length();i++){
                ans+=case2[i%2];
            }
        }
        cout << ans << endl;
        return 0;
    }
    
    int res = 0;
    for (int i=0; i<s.length(); i++){
        if ((i+1 < s.length()) && (i+2) < s.length() && s[i] == s[i+1] && s[i+1] == s[i+2])
        {
            vector<char> oldChars;
            oldChars.push_back(s[i]);
            s[i+1] = getDiffCh(oldChars);
            res+=1;
        }
        else {
            if (i+1 < s.length()){
                if (s[i+1] == s[i]){
                    vector<char> oldChars;
                    if (i-1 >= 0){
                        oldChars.push_back(s[i-1]);
                    }
                    oldChars.push_back(s[i+1]);
                    s[i] = getDiffCh(oldChars);
                    res+=1;
                }
            }
        }
    }
    cout << res << endl;
    cout << s << endl;
}