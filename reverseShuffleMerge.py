def reverseShuffleMerge(s):
    # We process the string in reverse to simulate rev(A)
    s = s[::-1]
    
    # total_count: frequency of each char in s
    total_count = Counter(s)
    
    # needed_count: frequency of each char required for the result string A
    # A consists of exactly half of the characters in s
    needed_count = {char: count // 2 for char, count in total_count.items()}
    
    # remaining_count: how many of each char are still available in s as we iterate
    remaining_count = dict(total_count)
    
    res = []
    
    for char in s:
        if needed_count[char] > 0:
            # Greedy step: 
            # Can we replace the last character in our result with the current 'char' 
            # to make the string lexicographically smaller?
            while res and res[-1] > char and remaining_count[res[-1]] > needed_count[res[-1]]:
                # If we pop it, we need to add it back to our 'needed' list
                popped_char = res.pop()
                needed_count[popped_char] += 1
            
            # Use the current character
            res.append(char)
            needed_count[char] -= 1
        
        # Always decrement the remaining count of the character we just passed over
        remaining_count[char] -= 1
            
    return "".join(res)
