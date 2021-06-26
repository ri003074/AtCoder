#include <iostream>
#include <string>
using namespace std;

int S;

int main()
{
    cin >> S;
    string s = to_string(S);

    int topping = 0;
    int i = 0;
    for (i = 0; i < 3; i++)
    {
        if (s[i] == 'o')
        {
            topping += 100;
        }
    }

    cout << 700 + topping << endl;
}