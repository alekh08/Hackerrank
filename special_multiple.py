from collections import deque

def special_multiple(N):
    # BFS queue starts with "9"
    queue = deque(["9"])
    visited = set()

    while queue:
        num = queue.popleft()
        remainder = int(num) % N

        if remainder == 0:
            return num

        if remainder not in visited:
            visited.add(remainder)
            queue.append(num + "0")
            queue.append(num + "9")

# Driver code for HackerRank input/output
if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        print(special_multiple(N))
