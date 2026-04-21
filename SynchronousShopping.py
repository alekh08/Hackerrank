import heapq
import sys

def solve():
    # Use fast I/O for large inputs
    input_data = sys.stdin.read().split()
    if not input_data: return
    idx = 0
    
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    centers = [0] * (n + 1)
    for i in range(1, n + 1):
        num_fish = int(input_data[idx]); idx += 1
        mask = 0
        for _ in range(num_fish):
            f_type = int(input_data[idx]); idx += 1
            mask |= (1 << (f_type - 1))
        centers[i] = mask
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Dijkstra
    num_masks = 1 << k
    dist = [[float('inf')] * num_masks for _ in range(n + 1)]
    
    # (time, node, mask)
    pq = [(0, 1, centers[1])]
    dist[1][centers[1]] = 0
    
    while pq:
        d, u, mask = heapq.heappop(pq)
        
        if d > dist[u][mask]:
            continue
            
        for v, w in adj[u]:
            nm = mask | centers[v]
            if dist[v][nm] > d + w:
                dist[v][nm] = d + w
                heapq.heappush(pq, (dist[v][nm], v, nm))
                
    # Final comparison
    target = num_masks - 1
    possible = []
    for mask in range(num_masks):
        if dist[n][mask] != float('inf'):
            possible.append((mask, dist[n][mask]))
            
    ans = float('inf')
    for i in range(len(possible)):
        m1, d1 = possible[i]
        for j in range(i, len(possible)):
            m2, d2 = possible[j]
            if (m1 | m2) == target:
                ans = min(ans, max(d1, d2))
                
    print(ans)

solve()
