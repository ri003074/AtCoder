#include <iostream>
using namespace std;

int N;
int A[110];

int max_diff = -1;
int min_val = -1;
int max_val = -1;
int diff = -1;
int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    min_val = A[0];
    max_val = A[0];

    for (int i = 0; i < N - 1; i++)
    {
        if (min_val > A[i + 1])
        {
            min_val = A[i + 1];
        }
        else if (max_val < A[i + 1])
        {
            max_val = A[i + 1];
        }

        // for (int j = 1; j < N; j++)
        // {
        //     diff = abs(A[j] - A[i]);

        //     if (diff > max_diff)
        //     {
        //         max_diff = diff;
        //     }
        // }
    }
    cout << max_val - min_val << endl;
}