#need to use recursion
def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    flatList = []
    for e in aList:
        if type(e) != list:
            flatList.append(e)
        else:
            flatList.extend(flatten(e))
    return flatList

# test run code
aList = [[4,5,1],['a',['b', ['c']]],'cat']
print(flatten(aList))

bList = [4,5,[1,'a',['cat'],2],[[[3]],'dog']]
print(flatten(bList))
