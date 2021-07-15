def test(n,a):
    lst = []
    ans = 0

    if n==3000 :
        ans = 3001
        return ans
    else:
        for i in range(3001):
            lst.append(False)

        for j in a:
            lst[j] = True

        for j in lst:
            ans = ans+1
            if j == False:
                return ans
                break

    

n = int(input(''))
a = list(map(int,input('').split(" ")))
a = [i-1 for i in a]

print(test(n,a))
