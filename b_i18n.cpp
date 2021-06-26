#include <iostream>
#include <string>
using namespace std;

string s;
int main()
{
    cin >> s;

    cout << s[0] + to_string(s.length() - 2) + s[s.length() - 1] << endl;
}