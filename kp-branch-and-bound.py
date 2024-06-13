from heapq import heappush, heappop
import time

def push(heap, item): # max heap
    heappush(heap, (-item[0], item[1]))

def pop(heap): # max heap
    item = heappop(heap)
    return (-item[0], item[1])

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def kp_greedy(sorted_array, capacity):
    profit = 0
    weight = 0
    for item in sorted_array:
        if weight + item.weight <= capacity:
            profit += item.profit
            weight += item.weight
    return profit

def kp_extended_greedy(sorted_array, capacity):
    max_profit = kp_greedy(sorted_array, capacity)
    for item in sorted_array:
        if item.weight <= capacity and item.profit > max_profit:
            max_profit = item.profit
    return max_profit

def kp_linear_relaxation(sorted_array, capacity):
    profit = 0
    weight = 0
    for item in sorted_array:
        if weight + item.weight <= capacity:
            profit += item.profit
            weight += item.weight
        else:
            profit += (capacity - weight) * item.profit / item.weight
            break
    return profit

def reject(branch, array, capacity, max_profit):
    weight = 0
    profit = 0
    for (x, p) in zip(array, branch):
        weight += x.weight * p
        profit += x.profit * p
    return weight > capacity or profit + kp_linear_relaxation(array[len(branch):], capacity - weight) < max_profit

def expand(branch):
    yield branch + [0]
    yield branch + [1]

def complete(branch, array):
    return len(branch) == len(array)

def cost(branch, array, parent_profit):
    return parent_profit + branch[len(branch) - 1] * array[len(branch) - 1].profit

def kp(array, capacity):
    max_profit = kp_extended_greedy(array, capacity)
    heap = []
    push(heap, (0, []))
    while len(heap) > 0:
        profit, solution = pop(heap)
        if reject(solution, array, capacity, max_profit):
            continue
        if complete(solution, array):
            if profit > max_profit:
                max_profit = profit
            continue
        for branch in expand(solution):
            push(heap, (cost(branch, array, profit), branch))
    return max_profit

array = [Item(10, 5), Item(20, 10), Item(30, 15), Item(40, 20), Item(51, 25)]
sorted_array = sorted(array, key=lambda x: x.profit / x.weight, reverse=True)
capacity = 50
start = time.time()
print(kp(sorted_array, capacity))
print(time.time() - start, "s", sep="")
