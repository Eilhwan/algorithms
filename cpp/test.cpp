
#include<iostream>

using namespace std;

int main(void)
{
    char *s = "EMMA";

    printf("%c\n", *(s));
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
    printf("%c\n", *(s + 3));
    
    
    return 0;
}