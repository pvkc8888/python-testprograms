import random, os, pprint


text = open("c:\\Users\\pvkc\\Desktop\\Mozart rolling dice.txt",'r') #opening the text file	
TotalMeasures = text.read().split("\n") 
Measures = [] 
for i in range(len(TotalMeasures)):  						#saving the initial measures
	Measures.append(TotalMeasures[i].split(" "))
#print(Measures[50])

givenlist = [[96,32,69,40,148,104,152,119,98,3,54], 		#Given list for dice combinations	
			[22,6,95,17,74,157,60,84,142,87,130],
			[141,128,158,113,163,27,171,114,42,165,10],
			[41,63,13,85,45,167,53,50,156,61,103],
			[105,146,153,161,80,154,99,140,75,135,28],
			[122,46,55,2,97,68,133,86,129,47,37],
			[11,134,110,159,36,118,21,169,62,147,106],
			[30,81,24,100,107,91,127,94,123,33,5],
			[70,117,66,90,25,138,16,120,65,102,35],
			[121,39,136,176,143,71,155,88,77,4,20],
			[26,126,15,7,64,150,57,48,19,31,108],
			[9,56,132,34,125,29,175,166,82,164,92],
			[112,174,73,67,76,101,43,51,137,144,12],
			[49,18,58,160,136,162,168,115,38,59,124],
			[109,116,145,52,1,23,89,72,149,173,44],
			[14,83,79,170,93,151,172,111,8,78,131]]

new_measure = []
roll = 0
for i in range(16):									#Calculating the new compose by rolling dice
	roll  = random.randrange(1,11)
	new_measure.append(givenlist[i][roll])
#print(new_measure)
sliced_measures = {}
n=1
for i in range(len(Measures)):						#Slicing the intial list into different measures of 3
	if float(Measures[i][1])<3*n:
		if not n in sliced_measures:
			sliced_measures[n] = [Measures[i]]
		else:
			sliced_measures[n].append(Measures[i])
	else:
		n = n+1
#print(sliced_measures)
new_compose = {}									#selecting the new compose lines and saving in new dict
for i in new_measure:
	new_compose[i] = sliced_measures[i]
for items in range(len(new_measure)):
	print(new_measure)
	new_measure[items] = new_measure[items]*3-3
i =0
time=0
for k,v in new_compose.items():						
	for items in range(len(new_compose[k])):
		#print(new_compose[k][items][1]) 
		new_compose[k][items][1] = -float(new_measure[i])+float(new_compose[k][items][1])+time
		#print(new_compose[k][items][1])
	i = i+1
	time = time+3


for items in new_compose.keys():
	for item in new_compose[items]:
		print(item)
  		#
new_compose_file = open("c:\\Users\\pvkc\\Desktop\\Mozart rolling dice modified.txt",'w')

for items in new_compose.keys():
	for values in range(len(new_compose[items])):
		for strings in new_compose[items][values]:
			#print(strings)
			new_compose_file.write("%s " % strings)
		new_compose_file.write("\n")
new_compose_file.close()

