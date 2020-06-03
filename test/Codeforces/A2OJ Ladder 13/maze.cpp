//재귀를 오르내리면서 시간이 많이 걸리므로, BFS를 사용하기로한다.
#include <bits/stdc++.h>
using namespace std;

int cntOfCell;
int n,m,k;
bool visited[502][502];
char grid[502][502];
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
int cnt = 0;

void bfs(int startRow, int startCol, int listSize){
    queue<pair<int,int>> que;
    que.push(make_pair(startRow,startCol));
    visited[startRow][startCol] = true;
    cnt+=1;
    if (listSize == cnt){
        return;
    }
    while (que.size()>0){
        int r = que.front().first;
        int c = que.front().second;
        que.pop();

        for (int i=0; i<4; i++){
            int nr = r+dx[i];
            int nc = c+dy[i];
            if (grid[nr][nc] == '.' && visited[nr][nc] == false){
                que.push(make_pair(nr,nc));
                visited[nr][nc] = true;
                cnt+=1;
                if (cnt == listSize)
                    return;
            }
        }
    }
}

void printResult(){
    if (cnt > 0){
        for (int i=1; i<=n; i++){
            for (int j=1; j<=m; j++){
                if (grid[i][j] == '.' && visited[i][j] == false){
                    grid[i][j] = 'X';
                }
            }
        }
    }
    for (int i=1; i<=n; i++){
        for (int j=1; j<=m; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
}

int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> k;
    for (int i=0; i<m+2; i++){
        visited[0][i] = false;
        grid[0][i] = '#';
    }
    for (int i=0; i<n; i++){
        string row;
        cin >> row;
        grid[i+1][0] = '#';
        for (int j=0; j<m; j++){
            grid[i+1][j+1] = row[j];
        }
        grid[i+1][m+1] = '#';

        visited[i+1][0] = false;
        for (int j=0; j<m; j++){
            if (row[j] == '.'){
                cntOfCell += 1;
                visited[i+1][j+1] = false;
            }
        } 
        visited[i+1][m+1] = false;
    }
     
    for (int i=0; i<m+2; i++){
        grid[n+1][i] = '#';
        visited[n+1][i] = false;
    }

    if (k>0 && cntOfCell > 0){
        for (int i=1; i<=n; i++){
            for (int j=1; j<=m; j++){
                if (grid[i][j] == '.' && visited[i][j] == false){
                    bfs(i,j,cntOfCell-k);
                    if (cnt == cntOfCell - k){
                        printResult();
                        return 0;
                    }
                }
            }
        }
    }
    else
        printResult();

}