t=int(input())

c=[]

def deduct(a,b,c):
	for i in range(a,b,1):
		if c[i]!=0:
			c[i]=c[i]-1
			
			
for i in range(t):
	p=[]
	profit=0
	n=int(input())
	p=input().split()
	for i in range(n):
		p[i]=int(p[i])

	
	for i in range(len(p)):
		if p[i]!=0:
			profit=profit+p[i]
			deduct(i+1,len(p),p)
	
	print(profit%1000000007)				
	
	