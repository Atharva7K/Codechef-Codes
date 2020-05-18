a,b=input().split()


la=list(a)
lb=list(b)
l1=len(la)
l2=len(lb)

la.sort()

k=0
c=[]
beg=True

if l1!=l2:
	print('-1')

else:		
	for i in range(l2):
		for j in range(l1):
			
			if beg==True and la[j]==0:
				beg=False
				continue
			elif la[j]>=lb[i]:
				c.append(la[i])
				break
			else:
				continue
print(c)			
				
			
		