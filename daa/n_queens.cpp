#include <iostream>
#include <vector>

using namespace std;

bool isSafe(const vector<int> &positions, const int row, const int col);
bool solveNQueens(vector<int> &positions, int row);
void displayBoard(const vector<int> &positions);

int main(int argc, char ** argv) {

    int n;
    cout<<"Enter the size of Board (nxn): ";
    cin>>n;

    int row, col;
    cout<<"Enter the position of first Queen to be placed: ";
    cin>>row>>col;


    vector<int> positions(n, -1);
    positions[row-1] = col-1;

    if(solveNQueens(positions, 0))
        displayBoard(positions);
    else 
        cout<<"No solution possible!"<<endl;

    return 0;
}

bool isSafe(const vector<int> &positions, const int row, const int col) {
    // write the code here
    for(int i=0; i<positions.size(); i++) 
    {
        if(positions[i] == -1)
            continue;
        if(positions[i] == col)
            return false;
        if(i-row == positions[i]-col)
            return false;
        if(i-row == col-positions[i])
            return false;
    }
    return true;
}

bool solveNQueens(vector<int> &positions, int row) {
    if(row >= positions.size())
        return true;
    if(positions[row] != -1)
        return solveNQueens(positions, row+1);
    for(int col = 0; col < positions.size(); col++)
    {
        if(isSafe(positions, row, col))
        {
            positions[row] = col;
            if(solveNQueens(positions, row+1))
                return true;
            positions[row] = -1;
        }
    }
    return false;
}

void displayBoard(const vector<int> &positions) {
    for(int i=0; i<positions.size(); i++)
    {
        for(int j=0; j<positions.size(); j++)
            cout<<((positions[i] == j) ? 'Q' : '_')<<"|";
        cout<<endl;
    }
}




// Design n-Queens matrix having first Queen placed. Use backtracking to place remaining
// Queens to generate the final n-queen‘s matrix.
