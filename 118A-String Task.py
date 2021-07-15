def string_task(inp):
    inp = inp.lower()
    s = ''
    for i in inp:
        if i=='a' or i=='y' or i=='o' or i=='e' or i=='u' or i=='i':
            continue
        else:
            s = s + '.'
            s = s + i

    print(s)
    return

inp = input('')
string_task(inp)

            

