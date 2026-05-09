class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            elems = []

            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            for j in range(left, right):
                elems.append(grid[top][j])

            for i in range(top, bottom):
                elems.append(grid[i][right])

            for j in range(right, left, -1):
                elems.append(grid[bottom][j])

            for i in range(bottom, top, -1):
                elems.append(grid[i][left])

            rot = k % len(elems)
            rotated = elems[rot:] + elems[:rot]

            idx = 0

            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1

            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid