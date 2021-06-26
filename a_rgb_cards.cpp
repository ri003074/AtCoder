#include <iostream>
using namespace std;

int A, B, C;
int main()
{
    cin >> A >> B >> C;

    int total = A * 100 + B * 10 + C;

    if (total % 4 == 0)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    return 0;
}