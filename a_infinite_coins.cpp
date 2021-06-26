#include <iostream>
using namespace std;

int N;
int A;

int main()
{
    cin >> N;
    cin >> A;

    if (N % 500 <= A)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    return 0;
}