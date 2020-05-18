t=int(input())

for i in range(t):
	p=[]
	profit=0

	
	n=int(input())
	p=input().split()
	for i in range(n):
		p[i]=int(p[i])

	
	p.sort()
	p.reverse()
	
	
	
	
		
	for i in range(len(p)):
		if p[i]==0 or p[i]-i<0:
			break
		else:	
			profit=profit+(p[i]-i)
	print(profit%1000000007)				

	
					
	
	