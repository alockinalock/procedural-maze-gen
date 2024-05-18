class generate:
    def __init__(self):
        pass

    def grid_init(self, x, y):
        length = y * 2 + 1
        width = x * 2 + 1

        grid = []
        for _ in range(width):
            row = []
            for _ in range(length):
                row.append(True)
            grid.append(row)

        return grid
