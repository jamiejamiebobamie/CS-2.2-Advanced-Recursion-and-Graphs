http://www.techiedelight.com/rot-cutting/
--------------
"Given a rod of length n and a list of prices of length i where 1 <= i <= n,
find the optimal way to cut [the] rod into smaller rods in order to maximize profit.""

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

5 Steps of Dynamic Programming:

1. Identify the subproblems:
    how much do each of the pieces of wood add up to after being cut?

2. Guess first choice
    first choice is to not cut the piece of wood and look up its value (if it exists)

3. Recursively define the value of an optimal solution
    the continually increasing maximum of recursively calling the function

4. Compute the value of an optimal solution (recurse and memoize)
    Store the combined value of the cut pieces (1 piece of wood cut == two pieces) for lookup.

5. Solve original problem - reconstruct from the sub-problems
    what's the max value of all the ways you can cut the piece of wood.


NOTE: For this problem there is only an array of prices. The lengths for each price are equal to index in the array + 1.
