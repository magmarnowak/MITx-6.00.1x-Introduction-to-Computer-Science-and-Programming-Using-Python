# MIT's solution
def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)

# test run code
aList = [[4,5,1],['a'],'cat']
print(flatten(aList))

aList = [4,5,[1,'a',['cat'],2],[[[3]],'dog']]
print(flatten(aList))
