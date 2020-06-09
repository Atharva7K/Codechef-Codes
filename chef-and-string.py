t=int(input())

for i in range(t):
	l=input()
	s=list(l)
	i=0
	count=0
	if len(s)==2 and s[i]!=s[i+1]:
		print(1)
		
	elif len(s)==2 and s[i]==s[i+1]:
		 print(0)	
		 

	else:	
		while i<len(s):
			if i== len(s)-1:
				break
				
			if s[i]!=s[i+1]:
				count=count+1
				i=i+2
			else:
				i=i+1
		print(count)	
				
				
			
				
		