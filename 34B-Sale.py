n , m = map(int,input("").split(" "))
lst_2 = []
ans = 0
t = 0
lst_1 = list(map(int,input("").split(" ")))

if m < n:
    for j in lst_1:
        if j <= 0:
            lst_2.append(j)
            t = t+1

    lst_2.sort()
    if len(lst_2) > 0 :
        if m<=t :
            for i in range(m):
                ans = ans + lst_2[i]
            print(abs(ans))
        else:
            for i in range(t):
                ans = ans + lst_2[i]
            print(abs(ans))
    else:
        print(abs(ans))


if m==n :
    for j in lst_1:
        if j <= 0:
            lst_2.append(j)

    lst_2.sort()
    for i in range(len(lst_2)):
        ans = ans + lst_2[i]

    print(abs(ans))

    

 