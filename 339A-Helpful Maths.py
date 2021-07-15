s = input("")
one = 0
two = 0
three = 0
ans = ""


for i in s:
    if i=='1':
        one = one+1
    if i=='2':
        two = two+1
    if i=='3':
        three = three+1


for a in range(one):
    ans = ans + "+"+"1"

for b in range(two):
    ans = ans + "+"+"2"

for c in range(three):
    ans = ans + "+"+"3"

answer = ans[1:]
print(answer)


