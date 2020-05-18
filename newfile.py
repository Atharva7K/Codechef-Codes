t=int(input())
a=[]
b=[]
j=0
for i in range(t):
	n=int(input())
	a=input().split()
	
	
	
	for i in range(len(a)):
		if a[i]=='1':
			j=j+1
			b[j]=i
			
	print(b)		
	
	