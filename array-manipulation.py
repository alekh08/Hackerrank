import sys

def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for a, b, k in queries:
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    
    max_val = 0
    current = 0
    for i in range(n):
        current += arr[i]
        if current > max_val:
            max_val = current
    return max_val

if __name__ == '__main__':
    fptr = sys.stdout
    
    nm = input().rstrip().split()
    n = int(nm[0])
    m = int(nm[1])
    
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
