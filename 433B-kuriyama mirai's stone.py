def stone_costs(n,v,m):
    v_sort = sorted(v)
    ans = []

    for i in range(1,n):
        v[i] = v[i-1]+v[i]
        v_sort[i] = v_sort[i-1]+v_sort[i]


    for j in range(m):
        t , l ,r = map(int,input('').split(' '))
        l = l-1
        r = r-1

        if t==1:
            if l==0:
                ans.append(v[r])
            else:
                ans.append(v[r]-v[l-1])

        else:
            if l==0:
                ans.append(v_sort[r])
            else:
                ans.append(v_sort[r]-v_sort[l-1])

    for t in ans:
        print(t)



n = int(input(''))
v = list(map(int,input('').split(' ')))

m = int(input(''))

stone_costs(n,v,m)