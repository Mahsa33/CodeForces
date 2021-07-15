n = int(input(""))
min_time = 1000000001
lst = list(map(int,input('').split(" ")))
min_lst = min(lst)
min_cnt = lst.count(min_lst)

if min_cnt > 1 :
    print("Still Rozdil")
else:
    for i in range(len(lst)):
        if lst[i] < min_time :
            min_time = lst[i]
            min_index = i
    print(min_index+1)


