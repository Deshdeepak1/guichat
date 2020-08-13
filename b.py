def br(omsg):
    txts=omsg.split()
    l=['']
    i=0
    for txt in txts:
        if len(l[i]+txt+' ')<=25:
            l[i]+=txt+' '
        else:
            i+=1
            l.append('')
            l[i]=txt+' '
    return '\n'.join(l)
msg=input()
print(br(msg))
