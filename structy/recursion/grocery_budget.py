# Write a function, grocery_budget, that takes in grocery_list and a number budget.
# Every item in grocery_list is a pair containing the item name and price.
# Your function should return all possible ways to purchase items without spending more than the given budget.
# The order of the items in the return value does not matter.
# You cannot purchase an item more than once. You do not have to spend the budget fully.

def grocery_budget(grocery_list, budget):
    if budget < 0: # no valid way to buy groceries.
        return []
    if len(grocery_list) == 0: # no items to choose from.
        return [[]]
    
    current_item = grocery_list[0]
    remaining_items = grocery_list[1:]

    all_ways = []

    ways_with_current = grocery_budget(remaining_items, budget - current_item[1])
    for ways in ways_with_current:
        ways.append(current_item[0])
        all_ways.append(ways)

    ways_without_current = grocery_budget(remaining_items, budget)
    all_ways += ways_without_current
        
    return all_ways

def driver():
    res = grocery_budget([  
        ('eggs', 5),
        ('milk', 3),
        ('butter', 3)
    ], 7) # ->
    # [ 
    #   [ 'eggs' ], 
    #   [ 'butter', 'milk' ], 
    #   [ 'milk' ], 
    #   [ 'butter' ], 
    #   [] 
    # ] 
    print(res)