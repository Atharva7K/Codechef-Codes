#include <iostream>
using namespace std;

void deduct(long x, long size, long (&a)[size])
	{   cout<<"yo"<<endl;
		for (int i = x; i <= size; i++)
		{  
		
		if(a[size]==0){ continue;}
			
			else 
			{a[size] -= 1;}
		}
	}



int main()
{
	int t;

	cin >> t;

	while (t--)
	{
		long n;
		long long profit = 0;
		cin >> n;

		long p[n];

		for (int i = 0; i < n; i++)
		{
			cin >> p[i];
		}

		for (int i = 0; i < n; i++)
		{
			if (p[i] == 0)
			{
				continue;
			}

			else
			{
				profit += p[i];
				deduct(i + 1, n, &p);
			}
		}

		cout << profit << endl;
	}
	return 0;
}

