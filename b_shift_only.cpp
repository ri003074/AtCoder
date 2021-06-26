#include <iostream>
using namespace std;

int N;
int A[210];

int main()
{
    N = 3;
    A[0] = 16;
    A[1] = 12;
    A[2] = 24;

    int res = 0;

    while (true)
    {
        bool exist_odd = false;

        for (int i = 0; i < N; i++)
        {
            if (A[i] % 2 != 0)
            {
                exist_odd = true;
            }
        }

        if (exist_odd)
            break;

        for (int i = 0; i < N; i++)
        {
            A[i] = A[i] / 2;
        }
        res += 1;
    }
    cout << res << endl;
}