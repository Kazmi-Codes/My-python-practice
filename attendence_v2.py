students	=	[{
	"name":	"Ali",
	"marks": 85},
	{"name":	"Ahmed",
	"marks": 32},
{"name":	"Sara",
	"marks": 90}]
for	s	in	students:
	if	s["marks"]	>=	33:
		result	=	"Pass"
	else:
		result	=	"Fail"
	print(s["name"],"-",	result)
