names	=	["Ali","Usman","Ahmed","Bilal","Umair","Zain","Hamza","Hassan","Abdullah","Ibrahim"]
salaries	=	[50000,60000,55000,45000,70000,65000,48000,52000,60000,75000]
for	i	in	range(10):
		name	=	names[i]
		salary	=	salaries[i]
		if	(i+1)	%	2	==	0:
			print(f"Emp-{i+1}-{name}-Active-Salary:{salary}")
		else:
			print(f"Emp-{i+1}-{name}-On Leave-Salary:{salary}")
