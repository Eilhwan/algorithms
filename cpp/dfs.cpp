#include<stack>
#include<iostream>

using namespace std;

int[] dfs(int* arr, int start, bool[] visited)
{
    visited[start] = true;
    stack<int> st;
    st.push(start);
    while (!st.empty)
    {
        int var = st.pop();
        for(int i = 0; i < arr[var].length; i++)
        {
            if (visited[])
            {
                /* code */
            }
            

        }
        
    }
    
    
}

int main(void)
{

}