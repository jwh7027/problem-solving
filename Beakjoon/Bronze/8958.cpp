#include <bits/stdc++.h>

using namespace std;

int x;
string a;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> x;


	for (int i = 0; i < x; i++) {
		cin >> a;

		int count = 0;
		int score = 0;
		for (int j = 0; j < a.length(); j++)
		{
			if (a[j] == 'O')
			{
				count++;
				score += count;
			}
			else count = 0;
		}
		cout << score << "\n";
	}
}