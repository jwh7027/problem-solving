#include <bits/stdc++.h>

using namespace std;

int v, N;
int arr[100];

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int count = 0;

	cin >> N;
	for (int i = 0; i < N; i++) cin >> arr[i];
	cin >> v;

	for (int i = 0; i < N; i++) {
		if (arr[i] == v) {
			count += 1;
		}
	}
	cout << count;
}