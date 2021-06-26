#include <iostream>
using namespace std;

int N;
int counter = 0;
int max_val;
int res = 0;
int main()
{

    cin >> N;
    max_val = 0;
    for (int i = 1; i <= N; i++)
    {

        int val = i;
        counter = 0;
        while (true)
        {
            if (val % 2 != 0)
                break;
            else
                val = val / 2;
            counter += 1;
        }
        if (max_val <= counter)
        {
            max_val = counter;
            res = i;
        }
    }
    cout << res << endl;
}