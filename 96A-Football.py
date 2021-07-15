n = int(input(''))
lst = []
val = 0
dic = {}

for i in range(n):
    inp = input('')
    lst.append(inp)


for i in lst:
    for j in lst:
        if i == j:
            val = val + 1
    dic[i] = val       
    val = 0

keymax = max(dic,key=dic.get)
print(keymax)
    
