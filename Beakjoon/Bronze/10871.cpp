#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, X;
	cin >> N >> X;
	int* a = new int[N];

	for (int i = 0; i < N; i++)
	{
		cin >> a[i];

		if (a[i] < X) {
			cout << a[i] << " ";
		}
	}
	delete a;

	return 0;
}