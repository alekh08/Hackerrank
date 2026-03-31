import sys

def solve():
    # Read n and the array of components
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        line2 = sys.stdin.readline()
        if not line2:
            return
        d = list(map(int, line2.split()))
    except ValueError:
        return

    # Total sum of connected components
    total_components = 0

    def get_components_count(parent):
        """Counts unique roots in the DSU array."""
        count = 0
        for i in range(64):
            if parent[i] == i:
                count += 1
        return count

    def find(parent, i):
        if parent[i] == i:
            return i
        # Path compression is not strictly needed for 64 nodes, 
        # but helpful for speed.
        parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent, i, j):
        root_i = find(parent, i)
        root_j = find(parent, j)
        if root_i != root_j:
            parent[root_i] = root_j

    def backtrack(index, current_parent):
        nonlocal total_components
        
        # Base case: we've considered all integers in the input
        if index == n:
            total_components += get_components_count(current_parent)
            return

        # Option 1: Exclude d[index] from the subset
        backtrack(index + 1, list(current_parent))

        # Option 2: Include d[index] in the subset
        new_parent = list(current_parent)
        bits = []
        for b in range(64):
            if (d[index] >> b) & 1:
                bits.append(b)
        
        # Perform union on all bits set in d[index]
        if bits:
            for i in range(len(bits) - 1):
                union(new_parent, bits[i], bits[i+1])
        
        backtrack(index + 1, new_parent)

    # Initial state: 64 isolated nodes (each node is its own parent)
    initial_parent = list(range(64))
    backtrack(0, initial_parent)
    
    print(total_components)

if __name__ == "__main__":
    solve()
