from gen_knapsack import Thing, bruteKnapsack, greedy, buildThings

def run():
    """  
    main run for case in the lecture session
    """
    datas = {
        'wine' : [89, 123],
        'beer' : [90, 154],
        'pizza' : [30, 154],
        'burger' : [50, 354],
        'fries' : [90, 365],
        'coke' : [79, 150],
        'apple' : [90, 95],
        'donut' : [10, 195]
    }

    foods = buildThings(datas, cost_custom='calories')
    constraint = 750
    print(f'using Greedy to find best menu below {constraint} calories')
    print(f'\nusing greedy and values as key function:')
    greedyVal = greedy(foods, constraint, lambda x: x.getValue())
    
    total_value = 0
    total_calories = 0
    for food in greedyVal:
        total_value += food.getValue()
        total_calories += food.getCost()
        print(f'{food},')
    print(f'total value for greedy by value: {total_value}')
    print(f'total calories of greedy by value: {total_calories}')

    print(f'\nusing greedy and calories as key function: ')
    greedyCalories = greedy(foods, constraint, Thing.getCost, descending=False)
    total_calories = 0
    total_value = 0
    for food in greedyCalories:
        print(f'{food},')
        total_calories += food.getCost()
        total_value += food.getValue()
    print(f'total value for greedy by calories: {total_value}')
    print(f'total calories of greedy by calories: {total_calories}')

    print(f'\nusing Greedy by inverse calories as key function:')
    greedyInverse = greedy(foods, constraint, lambda x : (1 / x.getCost()))
    total_calories = 0
    total_value = 0
    for food in greedyInverse:
        print(f'{food},')
        total_calories += food.getCost()
        total_value += food.getValue()
    print(f'total value for greedy by inverse calories: {total_value}')
    print(f'total calories of greedy by inverse calories: {total_calories}')

    print(f'\nusing Brute Force to find best menu below {constraint} calories:')
    total_value, menuList = bruteKnapsack(foods, constraint, Thing.getValue, lambda x : x.getCost())
    total_calories = 0
    for food in menuList :
        print(f'{food}')
        total_calories += food.getCost()
    print(f'total value for Brute force algorithm: {total_value}')
    print(f'total calories for Brute force algorithm: {total_calories}')
    

if __name__ == '__main__':
    run()