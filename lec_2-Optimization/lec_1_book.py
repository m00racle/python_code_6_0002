from gen_knapsack import Thing, bruteKnapsack, greedy, buildThings, recursiveKnapsack, dynamicKnapsack

def run():
    """  
    main run for case in the lecture session
    """
    datas = {'clock' : [175, 10], 'painting' : [90, 9], 'radio' : [20, 4], 'vase' : [50, 2], 'book' : [10, 1], 'computer' : [200, 20]}

    foods = buildThings(datas, cost_custom='weight')
    constraint = 20
    print(f'using Greedy to find best menu below {constraint} kg')
    print(f'\nusing greedy and values as key function:')
    greedyVal = greedy(foods, constraint, lambda x: x.getValue())
    
    total_value = 0
    total_weight = 0
    for food in greedyVal:
        total_value += food.getValue()
        total_weight += food.getCost()
        print(f'{food},')
    print(f'total value for greedy by value: {total_value}')
    print(f'total weight of greedy by value: {total_weight}')

    print(f'\nusing greedy and weight as key function: ')
    greedyweight = greedy(foods, constraint, Thing.getCost, descending=False)
    total_weight = 0
    total_value = 0
    for food in greedyweight:
        print(f'{food},')
        total_weight += food.getCost()
        total_value += food.getValue()
    print(f'total value for greedy by weight: {total_value}')
    print(f'total weight of greedy by weight: {total_weight}')

    print(f'\nusing Greedy by inverse weight as key function:')
    greedyInverse = greedy(foods, constraint, lambda x : (1 / x.getCost()))
    total_weight = 0
    total_value = 0
    for food in greedyInverse:
        print(f'{food},')
        total_weight += food.getCost()
        total_value += food.getValue()
    print(f'total value for greedy by inverse weight: {total_value}')
    print(f'total weight of greedy by inverse weight: {total_weight}')

    print(f'\nusing Brute Force to find best menu below {constraint} kg:')
    total_value, menuList = bruteKnapsack(foods, constraint, Thing.getValue, lambda x : x.getCost())
    total_weight = 0
    for food in menuList :
        print(f'{food}')
        total_weight += food.getCost()
    print(f'total value for Brute force algorithm: {total_value}')
    print(f'total weight for Brute force algorithm: {total_weight}')

    # test real life run using recursive and dynamic knapsack
    print(f'\nusing Recursive to find best menu below {constraint} kg:')
    recConsider, racAvail, recTaken, recValue, recMemo = recursiveKnapsack(foods, constraint)
    for food in recTaken:
        print(f'{food}')
    print(f'total value using recursion: {recValue}')
    print(f'total weight: {constraint - racAvail}')
    print(f'calls: {recMemo["calls"]}')

    print(f'\nusing Dynamic to find best menu below {constraint} kg:')
    dynConsider, dynAvail, dynTaken, dynValue, dynMemo = dynamicKnapsack(foods, constraint)
    for food in dynTaken:
        print(f'{food}')
    print(f'total value using recursion: {dynValue}')
    print(f'total weight: {constraint - dynAvail}')
    print(f'calls: {dynMemo["calls"]}')
    print(f'pulls: {dynMemo["pull"]}')
    

if __name__ == '__main__':
    run()