#include <iostream>
using namespace std;

int main()
{
    int a, b;
    a = 1;
    b = 21;
    int c = a * b;

    if (c % 2 == 0)
        cout << "Even" << endl;
    else
        cout << "odd" << endl;
}