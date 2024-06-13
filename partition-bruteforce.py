def candidates(array):
    if len(array) == 0:
        yield []
        return
    for candidate in candidates(array[1:]):
        yield [False] + candidate
        yield [True] + candidate

def valid(solution, array):
    sum = [0, 0]
    for (n, p) in zip(array, solution):
        if p:
            sum[0] += n
        else:
            sum[1] += n
    return sum[0] == sum[1]

def partition(array):
    for solution in candidates(array):
        if valid(solution, array):
            return True
    return False

array = [1, 2, 3, 17, 10, 4, 3, 0]
print(partition(array))