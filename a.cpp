#include <iostream>
#include "func.hpp"
using namespace std;

int main()
{


    int N = 20;
    int A = 2;
    int B = 5;
    int res = 0;

    for (int i = 1; i <= N; i++)
    {
        int val = i;
        int sum = 0;
        int amari = 0;

        sum = find_some_of_digit(i);

        if (2 <= sum && sum <= 5)
        {
            res += i;
        }
    }
    cout << res << endl;
}