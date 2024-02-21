class Solution {
public:
    int countLiveNeighbor(vector<vector<int>>& tab, int indexRow, int indexCol){
        int liveStatus = 0;
        int checkRow[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int checkCol[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
        int maxRow = tab.size();
        int maxCol = tab[0].size();
        // Search for neighbors
        for(int i = 0; i < 8; i++){
            int row = indexRow + checkRow[i];
            int col = indexCol + checkCol[i];
            if(0 <= row && row < maxRow){ // check row condition
                if(0 <= col && col < maxCol){ // check col condition
                    if(tab[row][col] == 1) liveStatus++;
                }
            }
        }
        return liveStatus;
    }
    void gameOfLife(vector<vector<int>>& board) {
        vector<vector<int>> curr = board;
        int n = board.size(); // row
        int m = board[0].size(); // col
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                int neighStatus = countLiveNeighbor(curr, i, j);
                int cellStatus = board[i][j];
                if(cellStatus == 1){
                    // Case: live
                    if(neighStatus < 2) board[i][j] = 0; // Case 1
                    else if(neighStatus == 2 || neighStatus == 3) board[i][j] = 1; // Case 2
                    else if(neighStatus > 3) board[i][j] = 0; // Case 3
                }
                else{
                    // Case: die
                    if(neighStatus == 3) board[i][j] = 1;
                }
            }
        }
    }
};