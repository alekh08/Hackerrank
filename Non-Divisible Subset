def nonDivisibleSubset(k, s):
    
    # Initialize the remainder counts
    remainder_count = [0] * k
    
    # Count the occurrences of each remainder
    for num in s:
        remainder_count[num % k] += 1
    
    # Start with at most one element with remainder 0
    subset_size = min(remainder_count[0], 1)
    
    # Loop through pairs of remainders and add the maximum count
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            subset_size += max(remainder_count[i], remainder_count[k - i])
        else:
            # If i == k - i, we can only take one element from this group
            subset_size += min(remainder_count[i], 1)
    
    return subset_size
