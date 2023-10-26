#matriz quadrada III - beecrowd 1557
nums = []
while True:
    e = int(input())
    if e == 0:
        break
    else:
        nums.append(e)

def Show(a, m):
    form = len(str(m))
    for i in range(len(a)):
        linha = ''
        for s in a[i]:
            for e in range(form):
                linha += " "
            linha += str(s)
        print(linha)

for n in range(len(nums)):
    matriz = [[0 for x in range(nums[n])] for y in range(nums[n])]
    maior = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            x = 2**(i+j)
            matriz[i][j] = x
            if x > maior:
                maior = x
    Show(matriz, maior)
    print('')
    
