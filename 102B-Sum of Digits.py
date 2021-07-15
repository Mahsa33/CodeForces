n = input('')
lst = []
m = 0
t = 1
ans = 0 

for k in n:
    lst.append(int(k))


while t < len(lst):
    m = 0
    for i in lst:
        m = m + i 

    lst.clear()

    for j in str(m):
        lst.append(int(j))

    ans = ans + 1

print(ans)
    


   


