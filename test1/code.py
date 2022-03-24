def fac(jyl):
	try:
		jyl=int(jyl)
		if jyl>0:
			wwx=1
			for i in range(jyl):
				wwx=wwx*(i+1)
			print(wwx)
		else:
			print(f"The number is lower than 1")
	except ValueError:
		print(f"Type is error!")
	else:
		pass
	return;

file_path='test1.in'

with open(file_path) as file_object:
	for jyl in file_object:
		fac(jyl.rstrip())