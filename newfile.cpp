#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	int i,c;
	while (t--)
	{
		long  n, k;
		cin >> n >> k;
		long a[n], balance[n], b = 0;
		for ( i = 0; i < n; i++)
		{
			balance[i] = 0;
			cin >> a[i];
		}
	for (c = 0; c < n; c++)
		{
			b = 0;
			for (i = 0; i <= c; i++)
			{
				if (a[i] < k)
					b += a[i];
				else if (a[i] % k > 0)
					b += (a[i] % k);
			}
			balance[c] += b;
		}
		for (c = 0; c < n; c++)
		{
			for ( i = c + 1; i < n; i++)
			{
				if (a[i] < k)
					balance[c] -= (k-a[i]);
				else if (a[i] % k > 0)
				{
					int  result2 = (((a[i]/k) + 1) * k) - a[i];
					balance[c] -= result2;
				}
			}
		}
		for (i = 0; i < n; i++)
		{
			if (balance[i] < 0)
				continue;
			else
			{
				cout<<balance[i]<<endl;
				break;
			}
		}
	}
	return 0;
}

