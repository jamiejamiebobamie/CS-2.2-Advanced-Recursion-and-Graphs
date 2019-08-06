def driver_function(W , wt , val , n):
    """The driver function for possible memoization dictionary storage.
       DID NOT IMPLEMENT MEMOIZATION FOR THIS FUNCTION.
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

    item_weight_to_value = []
    for i, item_weight in enumerate(wt):
        item_weight_to_value.append("#: "+str(i)+", w: "+str(item_weight)+ ", v: " + str(val[i])+" ")


    return "For given input: knapsack-weight capacity: " + str(W)+ "\nItem weight and value: " + "| ".join(item_weight_to_value) + ". The max value is "+ str(maxValue)


val = [60, 100, 120, 230, 60, 30, 20, 10, 5, 190]
wt = [10, 20, 30, 40, 17, 16, 15, 1, 23, 22]
W = 50
n = len(val)
print(driver_function(W , wt , val , n))
