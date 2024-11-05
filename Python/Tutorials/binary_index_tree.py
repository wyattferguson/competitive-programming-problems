'''
Binary Index Tree (Fenwick Tree)
'''


class BinaryIndexTree():
    def __init__(self, list):
        # Tree is indexed at 1 not 0
        self.data = [0] + list
        for i in range(1, len(self.data)):
            bi = i + (i & -i)
            if bi < len(self.data):
                self.data[bi] += self.data[i]

    def prefix_query(self, i):
        """Computes prefix sum of up to including the i-th element"""
        i += 1
        result = 0
        while i:
            result += self.data[i]
            i -= i & -i
        return result

    def range_query(self, end_index, start_index):
        """Computes the range sum between two indices (both inclusive)"""
        return self.prefix_query(end_index) - self.prefix_query(start_index - 1)

    def update(self, i, add):
        """Add a value to the i-th element"""
        i += 1
        while i < len(self.data):
            self.data[i] += add
            i += i & -i


if __name__ == "__main__":
    arr = [1, 5, 6, 2]
    bit = BinaryIndexTree(arr)
