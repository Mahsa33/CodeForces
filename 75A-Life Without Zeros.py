a = int(input(''))
b = int(input(''))
c1 = a + b
c1 = str(c1)
c1 = c1.replace('0','')
c1 = int(c1)

a = str(a)
b = str(b)

a = a.replace('0','')
b = b.replace('0','')
a = int(a)
b = int(b)

c2 = a + b


if c1 == c2 :
    print('YES')
else:
    print('NO')


