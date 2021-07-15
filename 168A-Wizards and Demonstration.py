n , x , y = map(int,input('').split(" "))

s = (y * n)
if s % 100 !=0:
    s = int(s / 100)
    s = s+1

else :
    s = int(s / 100)

if s < x:
    ans = 0
else:
    ans = s - x
    
print(ans)