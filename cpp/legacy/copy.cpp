
#include<iostream>
#include<string>
#include<ctype.h>

using namespace std;


int get_int(string s){
    int num1;   
    cout << ("%s", s);
    cin >> num1;
    
    return num1;
}

string get_string(string s){

    string str1;
    cout << ("%s", s);
    cin >> str1;

    return str1;
}
int main(void){

    string s = get_string("s: ");
    string t = s;

    t.toupper(t[0]);

    cout << s;
    cout << t;
    
    return 0;
}