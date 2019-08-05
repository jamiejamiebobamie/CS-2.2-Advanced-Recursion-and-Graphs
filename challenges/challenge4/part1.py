"""Part 1: Solve the Knapsack Problem using Dynamic Programming.

In your README - Clearly define the problem. Give full credit to any references you use.
In your README - Define in words, the 5 steps of DP as applied to this problem.
Write a memoized recursive solution to this problem with hardcoded sample input of size 10.
You do not have to read sample data from a file. Write your code in knapsack.py and other files as needed.
Print the sample input and solution output similar to how it is shown below (your structure for storing input may be different).
For this input:
    List of items with size and value:
    [[size1, value1],[size2,value2 ],.....[size10, value10]]
    Size of knapsack: S

The solution to the knapsack problem is to take these items
    [[size3, value3], [size5,value5]"""


# items = [ [size1, value1], [size2,value2 ], [size3, value3], [size4, value4], [size5, value5], [size6, value6], [size7, value7], [size8, value8], [size9, value9], [size10, value10]]
items = [ [10, 45], [20, 67], [25, 2], [30, 55], [17, 12], [5, 13], [40, 50], [19, 22], [22, 60], [9, 12] ]

# print(len(items))

capacity = 50

# from the Advanced Recursion & Dynamic Programming - 2 slides
def knapsack(items, len_items, capacity):
    # print(items, len_items, capacity)
    if len(items):
        # store.append(items.pop())
        # item = store[len(store)-1]
        item = items.pop()

	# base case
    if len(items) <= 0 or capacity <= 0:
        return 0
    if item[0] > capacity:
        return knapsack( items[len_items:], len_items, capacity)

	#two choices
    len_items-=1
    value_without = knapsack( items[:len_items], len_items, capacity)
    value_with = knapsack(items[:len_items], len_items, capacity - item[0]) + item[1]

    return max(value_without, value_with)


print(knapsack(items, len(items), capacity))
