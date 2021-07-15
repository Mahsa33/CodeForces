def Array(n,lst):
    lst1 = [] ; lst2 = [] ; lst3 = []

    for i in lst:
        if i<0:
            lst1.append(i)
        if i>0:
            lst2.append(i)
        if i==0:
            lst3.append(i)

    if len(lst2) == 0:
        lst2.append(lst1.pop())
        lst2.append(lst1.pop())

    if len(lst1) %2 ==0:
        lst3.append(lst1.pop())

    print(len(lst1)," ".join(map(str,lst1)))
    print(len(lst2)," ".join(map(str,lst2)))
    print(len(lst3)," ".join(map(str,lst3)))

n = int(input(""))
lst = list(map(int,input("").split(" ")))
Array(n,lst)




