
#include<iostream>
#include<array>

using namespace std;

int main(void)
{
    std:array<int, 10> arr1;
    arr1[0] = 10;
    
    cout << arr1[0] << "배열의 1번 요소" << endl;

    array<int, 4> arr2 = {1, 2, 3, 4};

    cout << "arr2의 모든 원소:";

    for (int i = 0; i < arr2.size(); i++)
    {
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    try
    {
        cout << arr2.at(1) << endl;
        cout << arr2.at(4) << endl;
        
    }
    catch(const std::exception& e)
    {
        cout << "error" << endl;
    }
    
    return 0;
}

void print(array<int, 5> arr)
{
    for(auto ele : arr)
        cout << ele << ", ";
}