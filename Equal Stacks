def equalStacks(h1, h2, h3):
    # Compute the initial heights of each stack
    s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    
    # Use pointers for each stack
    i, j, k = 0, 0, 0
    
    # Reduce the height of the tallest stack until all are equal
    while not (s1 == s2 == s3):
        # Find the tallest stack and remove the topmost cylinder
        if s1 >= s2 and s1 >= s3:
            s1 -= h1[i]
            i += 1
        elif s2 >= s1 and s2 >= s3:
            s2 -= h2[j]
            j += 1
        else:
            s3 -= h3[k]
            k += 1
    
    # Return the equal height
    return s1
