#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a;
    cin >> a;

    cout << ((a >= 90) ? "A" : (a >= 80) ? "B" : (a >= 70) ? "C" : (a >= 60) ? "D" : "F");

    return 0;
}