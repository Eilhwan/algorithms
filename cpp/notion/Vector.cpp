
#include<vector>

using namespace std;


int main()
{
    vector<int> v(10, 5);
    
    v.insert(find(v.begin(), v.end(), 1), 10);
    
    
    return 0;
}
