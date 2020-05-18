class employee:
	salary=0
	def __init__(self):
		
		print('done')
			
	def salry(self):
			
		self.salary=self.salary+1
		print(self.salary)
	def __del__(self):
		print('destructed')
		print(self.salary)
obj=employee()
print(dir(obj))						