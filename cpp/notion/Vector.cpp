
#include <vector>
#include <string>
#include <iostream>

using namespace std;


int main()
{
    vector<int> v(10, 5);
    vector<int> vec;
    // vector<int> ve(10);
    // vector<int> vec = {1, 2, 3, 4, 5};
    
    
    // v.push_back(1);
    // v.insert(find(v.begin(), v.end(), 1), 10);
    // v.insert(v.begin(), 5);

    // v.pop_back();
    // v.erase(v.begin());
    // v.erase(v.begin() + 1, v.begin() + 4);

    // v.clear();
    v.reserve(100);
    for(int i = 0; i < 100 ; i++)
        v.push_back(i);
    v.erase(v.end(), v.end() - 5);
    for(int i = 0; v.size(); i++)
    {
        cout << i;
    }
    v.shrink_to_fit();
    for(int i = 0; v.size(); i++)
    {
        cout << i;
    }



    

    
    return 0;
}
