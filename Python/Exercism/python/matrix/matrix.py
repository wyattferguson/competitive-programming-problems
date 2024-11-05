class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        m = matrix_string.splitlines()
        for row in m:
            i = [int(item) for item in row.split()]
            self.matrix.append(i)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [x[index-1] for x in self.matrix]
