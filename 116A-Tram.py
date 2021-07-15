num = int(input(""))
count = 0
capacity = 0


for i in range(0,num):
    a , b = map(int,input().split(" "))
    count = count - a
    count = count + b
    capacity = max(capacity , count)

  

print(capacity)