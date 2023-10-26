#Analogimon - beecrowd 2520
import math

results = []
while True:
    try:
        sz_x,sz_y = input().split()
        arr = []

        pos_mon = (0,0)
        pos_player = (0,0)
        for i in range(int(sz_x)):
            arr.append(list(map(int,input().split())))

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    pos_player = (i,j)
                if arr[i][j] == 2:
                    pos_mon = (i,j)

        dist_horiz = math.dist([pos_player[0]],[pos_mon[0]])
        dist_vert = math.dist([pos_player[1]],[pos_mon[1]])

        results.append(int(dist_horiz+dist_vert))
    except EOFError:
        break
for i in results:
    print(i)
    

