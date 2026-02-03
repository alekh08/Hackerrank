import sys
from collections import defaultdict

def journeyToMoon(n, astronaut):
    graph = defaultdict(list)
    for a, b in astronaut:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * n
    components = []
    
    def dfs(node):
        stack = [node]
        visited[node] = True
        size = 1
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
                    size += 1
        return size
    
    for i in range(n):
        if not visited[i]:
            components.append(dfs(i))
    
    total_pairs = n * (n - 1) // 2
    same_country_pairs = sum(size * (size - 1) // 2 for size in components)
    return total_pairs - same_country_pairs

if __name__ == '__main__':
    fptr = sys.stdout
    
    np = input().split()
    n = int(np[0])
    p = int(np[1])
    
    astronaut = []
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))
    
    result = journeyToMoon(n, astronaut)
    fptr.write(str(result) + '\n')
    fptr.close()
