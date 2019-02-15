
#removes PUT
def rmPUT():
	file = 'access.log'
	with open(file) as fd:
		with open('PUT.log','w') as fo:
			for line in fd:
				if "PUT" in line:
					fo.write(line)

rmPUT()


