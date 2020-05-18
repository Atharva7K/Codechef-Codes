#include <iostream>
using namespace std;

int main()
{
	int t, n;
	cin >> t;
	while (t--)
	{
		cin >> n;
		int a[n];
		int cnt = 0, j = 0;
		int dec = 1;

		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			if (a[i] == 1)
			{
				cnt++;
			}
		}
		int b[cnt];

		for (int i = 0; i < n; i++)
		{
			if (a[i] == 1)
			{
				b[j] = i;
				j++;
			}
		}
		for (int i = 1; i < cnt; i++)
		{
			if (b[i] - b[i - 1] < 6)
			{
				dec = 0;
				break;
			}
		}
		if (dec == 0 || cnt == 0)
		{
			cout << "NO" << endl;
		}
		else
		{
			cout << "YES" << endl;
		}
	}

	return 0;
}
