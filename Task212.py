
#removes GET
def rmPOST():
	file = 'access.log'
	with open(file) as fd:
		with open('POST.log','w') as fo:
			for line in fd:
				if "POST" in line:
					fo.write(line)

rmPOST()


