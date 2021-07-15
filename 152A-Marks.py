n , m = map(int,input('').split((' ')))

string_arr = [input('') for i in range(n)]

lst = [] ; arr = []
i = j = 0
while(i < n):
    while(j < m):
        lst.append(string_arr[i][j])
        i +=1
        if i == n:
            arr.append(lst)
            j +=1
            i = 0

print(arr)









