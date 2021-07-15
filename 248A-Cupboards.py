num = int(input(""))
lists = []
lst2 = []
a = []
b = [] 
min_a = 0
min_b = 0

for i in range(1,num+1):
    lst1 = list(map(int,input().split(" ")))
    lists.append(lst1)


j = 0    
for j in lists:
    lst2 = j
    a.append(lst2[0])
    b.append(lst2[1])

a_zero = a.count(0)
a_one = a.count(1)
b_zero = b.count(0)
b_one = b.count(1)

if a_zero < a_one :
    min_a = a_zero
else:
    min_a = a_one

if b_zero < b_one :
    min_b = b_zero
else:
    min_b = b_one

t = min_a + min_b

print(t)


     





