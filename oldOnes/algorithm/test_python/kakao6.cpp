#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    for(int k = 0; k < skill.size(); k++)
    {
        int t = skill[k][0];
        int r1 = skill[k][1];
        int c1 = skill[k][2];
        int r2 = skill[k][3];
        int c2 = skill[k][4];
        int d = skill[k][5];
        
        for(int i = r1; i <= r2; i++)
        {
            for(int j = c1; i <= c2; j++)
            {
                if(t == 1)
                {
                    if (board[i][j] > 0 && board[i][j] - d <= 0)
                        answer += 1;
                    board[i][j] -= d;
                }
                else
                {
                    if (board[i][j] <= 0 && board[i][j] + d > 0)
                        answer -= 1;
                    board[i][j] += d;
                }
            }
        }
    }
    return board.size() * board[0].size() - answer;
}
