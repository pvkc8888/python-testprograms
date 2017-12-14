
#Solution for Medium #344 
# splitting the given data into a proper format
text = open("c:\\Users\\pvkc\\Desktop\\test.txt",'r')
GivenData = text.read().strip().split("\n")
available = GivenData[0][1:-1].split(" ")

#storing the data as a dictionary
TP = {"available":available}
i = 0 
for item in range(1,len(GivenData)):
	TP['P'+ str(i)] = GivenData[item][1:-1].split(" ")
	i = i+1
Process_list = []
done = 0

#looping through the dict to find the processing list
while done==0 :
	NotValid = 0
	for item in Process_list:
		try:
			TP.pop(item,None)
		except:
			pass

	for k,v in TP.items():
		if k == 'available':
			continue
		
		if int(TP[k][3]) <= int(TP['available'][0]) and int(TP[k][4]) <= int(TP['available'][1]) and int(TP[k][5]) <= int(TP['available'][2]):
			for i in range(3):
				TP['available'][i] = int(TP['available'][i]) + int(TP[k][3+i])			
			Process_list.append(k) 		

	if (len(Process_list)) == len(GivenData)-1:
		done = 1

	for k,v in TP.items():
		if k == 'available':
			continue
		
		if int(TP[k][3]) > int(TP['available'][0]) or int(TP[k][4]) > int(TP['available'][1]) or int(TP[k][5]) > int(TP['available'][2]):
			NotValid +=1

	if NotValid == len(TP.keys())-1:
		print('cant process :(')
		done = 1

print(Process_list)
