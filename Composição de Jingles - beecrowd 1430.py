#Composição de Jingles - beecrowd 1430

notas = {
    'W' : 1,
    'H' :  0.5,
    'Q' : 0.25,
    'E' : 0.125,
    'S' : 0.0625,
    'T' : 0.03125,
    'X' : 0.015625
}
results = []

while True:
    entrada = list(input().split('/'))
    if entrada[0] == '*':
        break
    certos = 0

    for i in entrada:
        soma = 0
        for l in i:
            soma += notas[l]
        if soma == 1:
            certos += 1
    results.append(certos)

for i in results:
    print(i)