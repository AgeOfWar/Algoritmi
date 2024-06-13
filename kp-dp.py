import time

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def kp(array, capacity):
    n = len(array)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if array[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - array[i - 1].weight] + array[i - 1].profit)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

array = [Item(10, 5), Item(20, 10), Item(30, 15), Item(40, 20), Item(51, 25)]
capacity = 50
start = time.time()
print(kp(array, capacity))
print(time.time() - start, "s", sep="")
