t = int(input(''))
lst = []
for i in range(t):
    a = int(input(''))
    lst.append(a)

for j in lst:
    if (360 % (180-j))==0 :
        print('YES')
    else:
        print("NO")