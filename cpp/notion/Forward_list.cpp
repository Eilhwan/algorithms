
#include <forward_list>
#include <string>
#include <iostream>


using namespace std;
void main()
{
    // forward_list<int> fwd = {1, 2, 3};
    std::forward_list<int> fwd = {1, 2, 3};
    
    auto it = fwd.begin();

    fwd.push_front(1);
    fwd.insert_after(it, 5);

    fwd.pop_front();
    fwd.erase_after(it);

    fwd.erase_after(it, fwd.end());

    fwd.sort();
    fwd.sort(greater<int>());

    fwd.reverse();
    fwd.unique();
    fwd.unique([](int a, int b)
    {
        return (b - a) < 2;
    })


}