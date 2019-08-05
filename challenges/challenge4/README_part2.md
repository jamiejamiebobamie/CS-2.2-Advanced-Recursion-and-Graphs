http://www.techiedelight.com/rot-cutting/

Given a rod of length n and a list of prices of lenght i where 1 <= i <= n, find the optimal way to cut [the] rod into smaller rods in order to maximize profit.

Example:
    Input:
        length = [1,2,3,4,5,6,7,8]
        price = [1,5,8,9,10,17,17,20]
        rod_length = 4

    Best: Cut the rod into two pieces of length 2 each to gain revenue of 5+5 = 10

    Cut     Profit
    4       9
    1,3     (1+8) = 9
    2,2     (5+5) = 10
    3,1     (8+1) = 9
    1,1,2   (1+1+5) = 7
    1,2,1   (1+5+1) = 7
    2,1,1   (5+1+1) = 7
    1,1,1,1 (1+1+1+1) = 4

    Solution psuedocode (from website):
    rodcut(n) = max {price[i-1] + rodCut(n-1)} where 1 <= i <= n





https://docs.google.com/presentation/d/1QoK6PMX0eiJ6XEQsKa5ZkU-_EJHZ-uG1Pc6attOBkAQ/edit#slide=id.g5e24cbf5a7_0_100:
5 Steps of Dynamic Programming:

1. Identify the subproblems:
    how much do the two pieces of wood add up to for a given cut?

2. Guess first choice
    first choice is to not cut the piece of wood and look up its value (if it exists)

3. Recursively define the value of an optimal solution
    the max return value from the two pieces of wood produced from the cut

4. Compute the value of an optimal solution (recurse and memoize)
    sort the cut-lengths and store them for lookup.
    sort the current cuts and if their sorted tuple exists in the lookup, then continue

5. Solve original problem - reconstruct from the sub-problems
    what's the max value of all the cuts in the stored cuts
