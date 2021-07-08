#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>

bool leaner_search(int N, std::vector<int>& S)
{
    for (int i : S)
    {
        if (i == N)
            return true;
    }
    return false;
}

bool binary_search(int N, std::vector<int>& S)
{
    auto first = S.begin();
    auto last = S.end();

    while (true)
    {
        auto range_length = std::distance(first, last);
        auto mid_element_index = first + std::floor(range_length / 2);
        auto mid_element = *(first + mid_element_index);

        if (mid_element == N)
            return true;
        else if (mid_element > N)
            std::advance(last, -mid_element_index);
        if (mid_element < N)
            std::advance(first, mid_element_index);

        if (range_length == 1)
            return false;

    }
    

}
int main(int argc, char const *argv[])
{
    std::cout << "hello world!" << std::endl;

    
    return 0;
}
