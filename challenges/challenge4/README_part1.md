https://docs.google.com/presentation/d/1QoK6PMX0eiJ6XEQsKa5ZkU-_EJHZ-uG1Pc6attOBkAQ/edit#slide=id.g5e24cbf5a7_0_100:

5 Steps of Dynamic Programming:

1. Identify the subproblems:
    what are the weights and the values of the knapsack if the current item IS and IS NOT add to the knapsack

2. Guess first choice
    item := items[0]
    (the first item in the rucksack)

3. Recursively define the value of an optimal solution
    is this too much weight? (for each item)

4. Compute the value of an optimal solution (recurse and memoize)
    store the weight of the knapsack for each grouping of items

5. Solve original problem - reconstruct from the sub-problems
    what's the max value under 50 pounds
