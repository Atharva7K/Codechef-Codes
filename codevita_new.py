x,y=input().split()
x,y=int(x),int(y)
c=list()

sa=str(x)
a=list(sa)
sb=str(y)
b=list(sb)


l1=len(a)
l2=len(b)

def convert(list): 
	 res = sum(d * 10**i for i, d in enumerate(list[::-1])) 

	 return(res) 		

def calculate(a,b,l1,l2):
	for j in range(len(b)):
		for i in range(len(a)):
			if a[i]>=b[j]:
				c.append(a[i])
				a.remove(a[i])
				break
	if len(c)!=len(b):
		print('-1')
	else:
		print(convert(c))			

						
						

a.sort()

if l1<l2:
	print('-1')
elif l1>l2:
	a.sort()
	print(x)	
	

elif a[l1-1]<b[0]:
	print('-1')


		
else:	
	for i in range(l1):
		if a[i]==0:
			continue
		elif a[i]==b[0]:
			calculate(a,b,l1,l2)
			
			
			break
				
		elif a[i]>b[0]:
			c.append(a[i])
			a.remove(a[i])
			c=c+a
			print(convert(c))
			break


				
	
		