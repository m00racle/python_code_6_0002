import knapsack as kg

def opt_menu()->None:
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut']
    values = [89, 90, 30, 50, 90, 79, 90, 10]
    weights = [123, 154, 258, 354, 365, 150, 95, 185]
    maxWeight = 750

    # make Items.
    items = kg.buildItemsArgs(names, values, weights)

    # test run:
    print("Use Greedy algorithm optimize value: ", maxWeight)
    kg.printGreedy(items, maxWeight, kg.value)

    print("Use Greedy by weight to fill knapsack in size", maxWeight)
    kg.printGreedy(items, maxWeight, kg.weightInverse)

    print("Use Greedy by Density to fill knapsack in size", maxWeight)
    kg.printGreedy(items, maxWeight, kg.density)

    print("use knapsack 0/1 optimization with max constraing: ", maxWeight)
    kg.printOpt(items, maxWeight, lambda x: kg.Item.getValue(x), lambda y: kg.Item.getWeight(y))
    # we use lambda function this time to represent the getVal and getWeight function.


if __name__ == '__main__':
    opt_menu()
