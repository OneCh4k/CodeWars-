def xo(s):
    count_x, count_o = 0,0
    for i in list(s.lower()):
        if i.find('x'):
            count_x+=1
        if i.find('o'):
            count_o += 1
    if count_x == count_o:
        return True
    if count_x != count_o:
        return False