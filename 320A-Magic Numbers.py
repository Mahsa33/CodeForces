inp = input('')
cnt = len(inp)
b = 1
t = 0
s = '/'


inp = inp + s
for i in range(len(inp)):
    i = t
    if t == cnt :
        break
    if inp[i] =='1' and inp[i+1] =='4' and inp[i+2] =='4':
        t = t+3
    elif inp[i] =='1' and inp[i+1] =='4':
        t = t+2
    elif inp[i] =='1':
        t =t+1 
    else:
        b = 0
        break

if b == 0:
    print('NO')
else:
    print('YES')
