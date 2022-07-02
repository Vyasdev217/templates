import numpy as np
map=np.zeros((5,5))
for i in range(len(map)):
    map[i][0]=-1
    map[0][i]=-1
    map[i][len(map)-1]=-1
    map[len(map)-1][i]=-1
print(map)
