#include <string>
#include <iostream>
#include <forward_list>

using namespace std;

struct citizen
{
    string name;
    int age;
};

ostream &operator<<(ostream os, const citizen &c)
{
    return (os << "[" << c.name << ", " << c.age << "]" << endl);
}

void main()
{
    forward_list<citizen> citizens = {
        {"Kim", 22}, {"Lee", 18}, {"Jin", 16}
    };

    auto citizen_cp = citizens;

    cout << "전체 시민들: ";
    for(const auto &c : citizens)
        cout << c << " ";
    cout << endl;

    citizens.remove_if([](const citizen &k))
    {
        return (c.age < 19);
    }

    cout << "투표권이 있는 시민들: ";
    for(auto &c : citizens)
        cout << c << " ";
    cout << endl;

    



}