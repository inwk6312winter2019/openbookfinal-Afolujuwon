
#removes DELETE
def rmDELETE():
	file = 'access.log'
	with open(file) as fd:
		with open('DELETE.log','w') as fo:
			for line in fd:
				if "DELETE" in line:
					fo.write(line)

rmDELETE()


