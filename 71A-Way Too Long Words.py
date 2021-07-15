num = int(input(""))
lst = []
answer = ""
for i in range(num):
    word = input("")
    lst.append(word)


for j in lst:
    if len(j) > 10:
        first_lr = j[0]
        last_lr = j[-1]
        length = str(len(j)-2)
        answer = first_lr+length+last_lr
        print(answer)

    else:
        print(j)
        




