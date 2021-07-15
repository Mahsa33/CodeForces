num = int(input(""))
lst = list(map(int,input().split(" ")))
amazing = 0
max_lst = lst[0]
min_lst = lst[0]

for i in range(0,len(lst)):
    if  lst[i] < min_lst:
        min_lst = lst[i]
        amazing = amazing+1

    if  lst[i] > max_lst :
        max_lst = lst[i]
        amazing = amazing+1

print(amazing)

