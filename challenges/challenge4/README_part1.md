Problem Description:
    "Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property)."

        -https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

function inputs:


5 Steps of Dynamic Programming:

1. Identify the subproblems:
    what are the weights and the values of the knapsack if the current item IS and IS NOT added to the knapsack?
    Subproblem: Add it vs. don't add it.

2. Guess first choice
    item = items[0]
    (the first item in the rucksack)
    (just start somewhere)

3. Recursively define the value of an optimal solution
    is this too much weight for the knapsack? (for each item)

4. Compute the value of an optimal solution (recurse and memoize)
    store the weight of the knapsack for each grouping of items

5. Solve original problem - reconstruct from the sub-problems
    what's the max value that can be achieved under 50 pounds
