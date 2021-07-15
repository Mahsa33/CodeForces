s , n =list(map(int,input("").split(" ")))
lists = []
b = 0

for i in range(n):
    lst_1 = list(map(int,input('').split(" ")))
    lists.append(lst_1)

lists = sorted(lists)

for j in range(n):
    if s > lists[j][0] :
        s = s + lists[j][1]
    else :
        b = 1
        break

if b==1 :
    print('NO')
else:
    print('YES')






