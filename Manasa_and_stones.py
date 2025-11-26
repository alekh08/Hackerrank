def manasaAndStones(n, a, b):
    results = set()
    for x in range(n):
        value = x * a + (n - 1 - x) * b
        results.add(value)
    return sorted(results)

# HackerRank driver
if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        print(*manasaAndStones(n, a, b))
