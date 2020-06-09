t=int(input())
for i in range(t):
	sum1,sum2=0,0
	n,k=input().split()
	n,k=int(n),int(k)
	
	price=input().split()
	price=[int(x) for x in price]
	sum1=sum(price)
	
	for i in range(len(price)):
		if price[i]>k:
			price[i]=k
	sum2=sum(price)
	print(sum1-sum2)		