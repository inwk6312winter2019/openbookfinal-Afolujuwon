
#removes GET
def rmGET()
	file = 'access.log'
	with open(file) as fd:
		with open('GET.log','w') as fo:
			for line in fd:
				if "GET" in line:
					fo.write(line)

rmGET()


