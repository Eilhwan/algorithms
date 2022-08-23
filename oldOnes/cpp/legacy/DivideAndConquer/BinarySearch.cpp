
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>

using namespace std;

bool leaner_search(int N, vector<int>& S)
{
    for (int i : S)
    {
        if (i == N)
            return true;
    }
    return false;
}