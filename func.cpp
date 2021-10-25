#include <iostream>
#include <limits.h>
#include "func.hpp"
int find_some_of_digit(int n)
{
    int sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n = n / 10;
    }
    return sum;
}
bool palindromicNumber(int n)
{
    if (n == revInt(n))
    {
        return true;
    }
    else
    {
        return false;
    }
}

int revInt(int num)
{
    double rev = 0;
    while (num != 0)
    {
        rev = rev * 10 + num % 10;
        num = num / 10;
    }
    if (INT_MIN <= rev && rev <= INT_MAX)
    {
        return rev;
    }
    else
    {
        return 0;
    }
}