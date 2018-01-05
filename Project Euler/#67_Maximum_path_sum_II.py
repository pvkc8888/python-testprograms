t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    matrix = [[0 for x in range(n)]for y in range(n)]
    #print(matrix)
    for i in range(n):
        matrix[i] = list(map(int,input().split(' ')))
    total = 0
    for i in range(n-2,-1,-1):
        for col in range(i+1):
            #print(i,col)
            matrix[i][col] = matrix[i][col] + max(matrix[i+1][col],matrix[i+1][col+1])
    print(matrix[0][0])