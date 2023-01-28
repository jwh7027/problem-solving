#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int x, y;
	cin >> x >> y;

	if (x <= 2 && y >= 2) {
		cout << 2 << "\n";
	}

	for (int i = x; i <= y; i++) {
		for (int j = 2; j < i; j++) {
			if (i % j != 0) {
				if (i <= j * j) {
					cout << i << "\n";
					break;
				}
				else continue;
			}
			else break;
		}
	}

}