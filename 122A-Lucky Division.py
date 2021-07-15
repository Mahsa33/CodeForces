n = int(input(""))
a = [4,7,44,47,74,444,474,477,744,747,777,774]
b = False

for i in a:
    if n==i or n%i==0:
        b = True
        break
    else:
        b = False
        
if b == True :
    print('YES')
else:
    print('NO')


          
