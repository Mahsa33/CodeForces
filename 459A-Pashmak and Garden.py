x1 , y1 , x2 , y2 = map(int,input('').split(' '))

if x1!=x2 and y1!=y2 and (abs(x1-x2)!=abs(y1-y2)) :
    print(-1)

elif x1==x2 :
    a = abs(y1-y2)
    ans = f'{x1+a} {y1} {x2+a} {y2}'
    print(ans)


elif y1==y2 :
    a = abs(x1-x2)
    ans = f'{x1} {y1+a} {x2} {y2+a}'
    print(ans)


else:
    ans = f'{x1} {y2} {x2} {y1}'
    print(ans)
    