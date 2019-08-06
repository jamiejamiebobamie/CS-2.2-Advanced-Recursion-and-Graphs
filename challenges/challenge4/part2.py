def driver_function(prices,n):
    """The driver holds the lookup dictionary and makes the original function call to rodcut function.
    """
    dict = {}
    def rodcut(prices,n):
        """
            Note:
                this function was found in C++ on: https://www.techiedelight.com/rot-cutting/
            Input:
                an array of prices with indexes that correlate to the size of the pieces of wood.
                an integer of the length of the wood to be cut.
            Output:
                a string of the inputs and the resulting max cost that can be made from the length of the wood and the prices.
        """

        # each time the function gets called initialize maxValue to be negative infinity
        maxValue = float('-inf')

        # return 0 if the input length of the rod is 0 or if the input length is greater than the array as that will throw list index out of range errors below
        if n == 0 or len(prices) <= n:
            return 0

        # generate numbers between 1 and the current rod_length + 1 (+1 because range() is non-inclusive at the upper bounds)
        for _ in range(1, n+1):

            # set 'entry' to a tuple of the current cut. a cut consists of two pieces.
            # cut == piece A and piece B: A is: _ and piece B is: the length of the rod - piece A.
            cut = (_, n-_)

            # memoization dictionary:
            if cut in dict:
                cost = dict[cut]
            else:
            # reference the price for piece A, taking into account the index of piece A will be: _-1
            # need to determine the cost(s) of all pieces resulting from that cut.
            # so piece B is fed into "the wood chipper": the rodCut function, to determine its cost(s)
                cost = prices[_-1] + rodcut(prices, n - _)
                dict[cut] = cost

            # if the resuting cost is greater than the local maxValue set the local maxValue to the cost
            if (cost > maxValue):
                maxValue = cost

        # return the maxValue to the outside scope.
        return maxValue

    maxValue = rodcut(prices,n)
    printable_prices = [str(price) for price in prices]

    return "For this input:\n\n"+ "prices: " + ", ".join(printable_prices) + "\nwood length: " + str(n) + "\n\nThe solution is:\n\n" + str(maxValue)


# i + 1 == wood length:
# [1,2,3,4,5,6,7,8,9,10]
# example: a cut of wood of length 2 is 5 (dollars?)
prices = [1,5,8,9,10,17,17,20,24,26]

# the length of the piece of wood:
n = 4

print(driver_function(prices, n))
