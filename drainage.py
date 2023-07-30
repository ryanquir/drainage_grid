def max_run(grid):
    def dfs(i, j):
        longest_run = []
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] < grid[i][j]:
                run = dfs(x, y)
                if len(run) > len(longest_run):
                    longest_run = run
        return [(i, j)] + longest_run
    run_max = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            run = dfs(i, j)
            if len(run) > len(run_max):
                run_max = run
    for i, j in run_max:
        print(i, j)