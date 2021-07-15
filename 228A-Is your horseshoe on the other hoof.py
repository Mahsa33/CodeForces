lst = list(map(int ,input("").split(" ")))
num = 0

lst.sort()
for i in range(len(lst)):
    if lst[i] == lst[i+1]:
        num = num+1
    if i==2:
        break

print(num)
