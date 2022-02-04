def get_parts(n):
    if not n.isdigit():
        return 'please provide an valid integer number...'
    part = {
    'koti': 0,
    'lakh': 0,
    'hajar': 0,
    'sotok': 0,
    'akok':0,
    }
    def slice2(n):
        return n[:len(n)-2],n[len(n)-2:]
    def slice1(n):
        return n[:len(n)-1],n[len(n)-1:]

    if len(n)>2:
        n,l = slice2(n)
        part['akok'] = l
        if len(n) > 1:
            n,l = slice1(n)
            part['sotok'] = l
            if len(n) > 2:
                n,l = slice2(n)
                part['hajar'] = l
                if len(n) > 2:
                    n,l = slice2(n)
                    part['lakh'] = l
                    part['koti'] = n
                else:
                    part['lakh'] = n
            else:
                part['hajar'] = n
        else:
            part['sotok'] = n
    else:
        part['akok'] = n

    lst = []
    for i in part:
        lst.append(part[i])
    
    if len(str(lst[0])) > 2:
        lst[0] = get_parts(lst[0])
    units = [' koti, ',' lakh, ',' hajar, ',' soto, ','']
    text =''
    for (a,b) in zip(lst,units):
        if (a == 0) or (a == '0') or (a == '00'):
            continue
        text += str(a) + str(b)
    return text

part = get_parts(input('please input a valid input in integer num other than ""...\n'))
print(part)