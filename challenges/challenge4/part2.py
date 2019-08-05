# In your README - Clearly define the problem. Give full credit to any references you use.
# In your README - Define in words, the 5 steps of DP as applied to this problem.
# Write a memoized recursive solution to this problem with hardcoded sample input of size 10. You do not have to read sample data from a file. Write your code in dynamic_program.py and other files as needed.
# Print the sample input and solution output similar to how it is shown below with actual data from your problem.
# For this input:
#     XXXXX
#
# The solution is:
#     YYYYYYY



"""Example:
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
    1,1,1,1 (1+1+1+1) = 4"""

def findBestCut(length, price, rod_length, cut):
    # my attempt:
    if cut == 0:
        return
    if rod_length not in length:
        return
    else:
        findBestCut(length, price, rod_length, cut-1)

# C++ solution found on:
# https://www.techiedelight.com/rot-cutting/
def rodCut(prices,n, dict):
    """This is super cool, but I don't really understand this at all.
    """

    # if not maxValue:
    maxValue = float('-inf')

    if n == 0:
        return 0

    for _ in range(1, n+1):
        entry = (_-1, n-_)

        # memoization:
        if entry not in dict:
            cost = prices[_-1] + rodCut(prices, n - _, dict)
            dict[entry] = cost
        else:
            cost = dict[entry]

        if (cost > maxValue):
            maxValue = cost

    return maxValue

length = [1,2,3,4,5,6,7,8]
rod_length = 4

prices = [1,5,8,9,10,17,17,20]
# prices = [1,5,8,9,10,17,17,15]

n = 8

dict = {}
print(rodCut(prices, n, dict))
