t=int(input())
a=[]
for i in range(t):
	n=int(input())
	a=input().split()
	switch=0
	dec=1
	beg=0
	len=0
	last=0
	
	
	for i in range(n):
		if a[i]=='1':
			if switch==0:
				beg=i
				switch=1
			else:
				last=i
				switch=0
				len=last-beg
				if len<6:
					dec=0
					break
	if dec==0:
		print("NO")
	else:
		print("YES")						