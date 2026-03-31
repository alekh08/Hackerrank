def getMinimumCost(k, c):
    c.sort(reverse=True)
    total = 0
    
    for i in range(len(c)):
        total += (i // k + 1) * c[i]
    
    return total
