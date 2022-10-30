def spin_words(sentence):
    count=0 
    l = sentence.split()
    if len(l) == 1:
        if len(l[0]) >= 5:
            return l[0][::-1]
        else:
            return(''.join(l)) 
    elif len(l) > 1:
        for i in l:
            if len(i)>=5:
                l[count] = i[::-1]
            count+=1
        return ' '.join(l)