#O despertar da força - beecrowd 2163
x,y = input().split()
matriz = []
found = False
t = [[0 for a in range(int(y)+2)] for b in range(int(x)+2)]

for i in range(int(x)):
    entrada_linha = list(map(int,input().split()))
    matriz.append(entrada_linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        t[i+1][j+1] = matriz[i][j]

for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j] == 42:
            #check adjascent
            if t[i-1][j-1] == 7 and t[i-1][j] == 7 and t[i-1][j+1] == 7 and t[i][j-1] == 7 and t[i][j+1] == 7 and t[i+1][j-1] == 7 and t[i+1][j] == 7 and t[i+1][j+1] == 7:
                print(i,j)
                found = True
                break
if found == False:
    print(0,0)