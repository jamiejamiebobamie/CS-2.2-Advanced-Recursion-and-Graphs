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



def driver_function(W , wt , val , n):
    """The driver function for possible memoization dictionary storage.
    """
    def knapsack(W , wt , val , n):
        """ Code copied from:
                https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
            Input:
                W: A max weight of the carrying capacity of the knapsack
                wt: An array of integer weights of the items
                val: An array of integer values of the items
                n: An integer, the number of items

            Output:
                The max value that can be carried in the knapsack
        """

        # Base Case: if the number of items is zero or if the carryign capacity of the knapsack is 0
        if n == 0 or W == 0 :
            return 0

        # If weight of the nth item is more than knapsack's capacity
        # W, then this item cannot be included in the optimal solution.
        # Do not subtract the item's weight from W and move on to the next item.
        if (wt[n-1] > W):
            return knapsack(W , wt , val , n-1)

        # return the maximum of two cases: nth item included and not included
        else:
            return max(val[n-1] + knapsack(W-wt[n-1] , wt , val , n-1),
                       knapsack(W , wt , val , n-1))

    # call the knapsack function
    maxValue = knapsack(W , wt , val , n)

    item_weight_to_value_dictionary = {}
    for i, item_weight in enumerate(wt):
        item_weight_to_value_dictionary[str(item_weight)] = str(val[i])


    return "For given input: knapsack weight capacity: " + str(W)+ "item weight and value arrays: " + item_weight_to_value_dictionary+"\nthe max value is "+ str(maxValue)


val = [60, 100, 120, 230]
wt = [10, 20, 30, 40]
W = 50
n = len(val)
print(driver_function(W , wt , val , n))
