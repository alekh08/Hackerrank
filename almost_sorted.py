def almostSorted(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    
    # Find the indices where arr and sorted_arr differ
    diff = [i for i in range(n) if arr[i] != sorted_arr[i]]
    
    if not diff:
        print("yes")
    elif len(diff) == 2:
        print("yes")
        print(f"swap {diff[0]+1} {diff[1]+1}")
    else:
        i, j = diff[0], diff[-1]
        if arr[i:j+1] == sorted_arr[i:j+1][::-1]:
            print("yes")
            print(f"reverse {i+1} {j+1}")
        else:
            print("no")
