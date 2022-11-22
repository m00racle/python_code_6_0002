import knapsack as kg

def opt_menu()->None:
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
    values = [89,90,95,100,90,79,50,10]
    weights = [123,154,258,354,365,150,95,195]
    maxWeight = 1000

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
