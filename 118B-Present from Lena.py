n = int(input(""))
k = n
s = n-1
t = 0

for i in range(1,n+2):
    m = k
    while(m!=0):
        print('  ',end='')
        m = m-1
    if i==1:
        print("0")
    else:
        for j1 in range(0,n-s+1):
            print(j1,end=' ')
        for j2 in range(n-s-1,-1,-1):
            t = t+1
            if t>=1 and j2==0:
                print(j2,end="")
            else:
                print(j2,end=' ')
        s = s-1
        print("")
    k = k-1


s = n
t = 0 
j1 = 0
j2 = 0


for i in range(1,n+1):
    m = 1
    while(m <= i):
        print('  ',end="")
        m = m+1
    if i==n:
        print("0",end="")
    else:
        for j1 in range(0,s):
            print(j1,end=' ')
        for j2 in range(s-2,-1,-1):
            t = t+1
            if t>=1 and j2==0:
                print(j2,end="")
            else:
                print(j2,end=' ')
        s = s-1
        print("")  
    
    



        

