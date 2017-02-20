def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    listC =[]
    for  index in range(0, len(listA)):
        listC.append(listA[index]*listB[index])
    result = 0
    for x in listC:
        result += x
    return result
