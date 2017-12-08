def PrintTable(tableData,maximum):
	for i in range(len(tableData[1])):
		for y in range(len(tableData)):
			print(tableData[y][i].rjust(maximum),end = " ")
		print("\n")


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
maximum = 0
for i in range(len(tableData)):
	for y in range(len(tableData[1])):
		if maximum < len(tableData[i][y]):
			maximum = len(tableData[i][y])
PrintTable(tableData,maximum)