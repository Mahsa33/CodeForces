n = int(input(""))
num_0 = 0
num_5 = 0

lst = list(map(int,input("").split(" ")))
num_0 = lst.count(0)
num_5 = lst.count(5)

if num_0==0:
    print(-1)
elif num_5 < 9 :
    print(0)
else:
    num_5 = num_5 -  (num_5 % 9)
    for j in range(num_5):
        print(5,end="")
    for t in range(num_0):
        print(0,end="")