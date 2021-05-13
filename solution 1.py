def calculateSumAfterBefore(l):
    for i in range(0, len(l) + 1):
        if(sum(l[:i]) == sum(l[i+1:])):
            return i+1
    return -1


listOfInteger = [2, 2, 5, 3, 1]
print(calculateSumAfterBefore(listOfInteger))
