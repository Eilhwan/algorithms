
#include<iostream>
#include<array>

int main(int argc, char const *argv[])
{
    std::array<int, 5> arr1 = {1, 2, 3, 4, 5};

    std::cout << *(&arr1.front() + 1) << std::endl;
    std::cout << arr1.back() << std::endl;
    std::cout << *(arr1.data() + 1) << std::endl;
    return 0;
}
