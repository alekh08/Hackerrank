def get_pluses(grid):
    n, m = len(grid), len(grid[0])
    pluses = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'G':
                continue
            size = 0
            while True:
                if (i - size < 0 or i + size >= n or
                    j - size < 0 or j + size >= m or
                    grid[i - size][j] != 'G' or
                    grid[i + size][j] != 'G' or
                    grid[i][j - size] != 'G' or
                    grid[i][j + size] != 'G'):
                    break
                cells = {(i, j)}
                for k in range(1, size + 1):
                    cells.update([(i - k, j), (i + k, j), (i, j - k), (i, j + k)])
                pluses.append(cells)
                size += 1
    return pluses

def twoPluses(grid):
    pluses = get_pluses(grid)
    max_product = 0
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            if pluses[i].isdisjoint(pluses[j]):
                product = len(pluses[i]) * len(pluses[j])
                max_product = max(max_product, product)
    return max_product
