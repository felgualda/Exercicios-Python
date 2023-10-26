#Área Inferior - beecrowd 1188
op = input()
arr = [[0 for x in range(12)] for y in range(12)]

for i in range(12):
    for j in range(12):
        arr[i][j] = float(input())

soma = 0
for i in range(7,11):
        soma += (arr[i][5] + arr[i][6])
        for k in range(i-7):
            soma += (arr[i][5-k] + arr[i][6+k])

if op == 'S':
    print('{:.1f}'.format(soma))
if op == 'M':
    print('{:.1f}'.format(soma/30))