lst = []
ans = False
n = int(input(''))

for i in range(n):
    a , b = map(int,input('').split(" "))
    lst.append([a,b])

lst.sort()

for j in lst:
    if j[0] < j[1]:
        ans = True

if ans==True :
    print('Happy Alex')
else:
    print('Poor Alex')


