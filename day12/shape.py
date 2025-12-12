class Shape:
    def __init__(self, i, input: list[str]) -> None:
        self.id = i
        self.size = 0
        self.shape = [[0 for _ in range(3)] for _ in range(3)]
        for i,line in enumerate(input):
            for j,char in enumerate(line):
                if char == '#':
                    self.shape[i][j] = 1
                    self.size += 1