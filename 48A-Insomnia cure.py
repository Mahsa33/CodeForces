k = int(input(""))
l = int(input(""))
m = int(input(""))
n = int(input(""))
d = int(input(""))
ans = 0;ans1=0



if k==1 or l==1 or m==1 or n==1:
    ans = d
else:
    for i in range(1,d+1):
        if i%k!=0 and i%l!=0 and i%m!=0  and i%n!=0 :
            ans1 = ans1+1
    ans = d-ans1

print(ans)
