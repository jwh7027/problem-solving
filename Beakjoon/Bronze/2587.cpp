#include <bits/stdc++.h>

using namespace std;

int arr[5], avg;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	for (int i = 0; i < 5; i++) { cin >> arr[i]; }
	for (int i = 0; i < 5; i++) { avg += arr[i]; }
	cout << avg / 5 << "\n";
	sort(arr, arr + 5);
	cout << arr[2];
}