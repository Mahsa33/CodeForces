s = input("")
t = input("")

s_len = len(s)
s_revers = s[s_len :: -1]

if s_revers==t :
    print('YES')
else :
    print('NO')