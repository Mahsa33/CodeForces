x , y , a , b = map(int,input('').split(' '))
ans = 0

for i in range(a,x+1):
    for j in range(b,y+1):
        if i > j :
            ans = ans+1
print(ans)

for i in range(a,x+1):
    for j in range(b,y+1):
        if i > j :
            print(f'{i} {j}')