#include <iostream>
#include <string>
using namespace std;

string S;

int main()
{
    cin >> S;
    S = S.replace(0, 4, "2018");

    cout << S << endl;
}