
l1 =[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,1,2,3,4,5,6,7,8,1,2,3,4,5,6]

map = {}

for n in l1:
    if n not in map:
        map[n] = 1
    else:
        map[n] += 1

print(map)
