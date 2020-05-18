t=int(input())
n=int(input())
cnt=1
diff=list()
dec=0
i=0


for i in range(t):
	y=input()
	x=y.split()
	for i in range(len(x)):
		x[i]=int(x[i])
		
	

	cnt=1		
	for i in range(i,len(x)-1):
		if x[i+1]-x[i]<=2:
			cnt=cnt+1
			print(cnt)
		else:
			print(x[i+1],x[i])
			diff.append(cnt)
			cnt=1
			
				

	
	
	
	
		
			
			
					
