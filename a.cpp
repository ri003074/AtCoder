#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include "func.hpp"
using namespace std;

int main()
{
    // int N = 4;
    // int M = 3; //road count
    // int IN[3][2] = {{1, 2}, {2, 3}, {1, 4}};

    // int N = 2;
    // int M = 5;

    // int IN[5][2] =
    //     {
    //         {1, 2},
    //         {2, 1},
    //         {1, 2},
    //         {2, 1},
    //         {1, 2},
    //     };

    int N = 8;
    int M = 8; //road count
    int IN[8][2] =
        {

            {1, 2},
            {3, 4},
            {1, 5},
            {2, 8},
            {3, 7},
            {5, 2},
            {4, 1},
            {6, 8},
        };

    vector<int> total;

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            total.push_back(IN[i][j]);
        }
    }

    int res[100];
    for (int i = 0; i < 100; i++)
    {
        res[i] = 0;
    }

    for (int i = 0; i < total.size(); i++)
    {
        res[total[i]]++;
    }

    for (int i = 1; i < N + 1; i++)
    {
        cout << res[i] << endl;
    }
}
