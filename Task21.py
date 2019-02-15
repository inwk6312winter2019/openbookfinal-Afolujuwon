def getLogs():
	
	with open('access.log','r') as file:
		file_split = line.split()
		if char in file_split == 'GET':
			GETlog.write(file_split)


getLogs()
