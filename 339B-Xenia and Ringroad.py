n , m = map(int,input('').split(' '))
loc = 1
ans = 0
inp = list(map(int,input('').split(' ')))

for a in inp:
    if a >= loc :
        ans += a - loc
    else :
        ans += n - (loc - a)
    loc = a

print(ans)
    
