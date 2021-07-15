def puzzles(n,m,lst):
    lst.sort()
    ans = lst[n-1] - lst[0]

    for i in range(1,m-n+1) :
       if (lst[i+n-1] - lst[i] < ans):
           ans = lst[i+n-1] - lst[i]


    return ans

n , m = map(int,input('').split(' '))
lst = list(map(int,input("").split(" ")))

print(puzzles(n,m,lst))
