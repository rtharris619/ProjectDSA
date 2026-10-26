# Write a function, lining_up, that takes in a list of people and a capacity number.
# We need to add people to the waitlist for a popular restaurant, but space is limited.
# The function should return a 2D list containing all the possible orders by which the people can line up.
# A valid line must be filled up exactly to the capacity.

# O (n! / (n - k)!)
def lining_up(people, capacity):    
    if capacity > len(people): # not possible to generate these lines.
        return []
    if capacity == 0: # a line containing nobody.
        return [[]]
    
    current_person = people[0]
    remaining_people = people[1:]

    all_lines = []

    for line in lining_up(remaining_people, capacity - 1):
        for i in range(len(line) + 1):
            all_lines.append(line[:i] + [current_person] + line[i:])

    all_lines += lining_up(remaining_people, capacity)

    return all_lines

def driver():
    res = lining_up(["jason", "jen", "cody", "vicky"], 3) # ->
    # [ 
    #   [ 'jason', 'jen', 'cody' ], 
    #   [ 'jen', 'jason', 'cody' ], 
    #   [ 'jen', 'cody', 'jason' ], 
    #   [ 'jason', 'cody', 'jen' ], 
    #   [ 'cody', 'jason', 'jen' ], 
    #   [ 'cody', 'jen', 'jason' ], 
    #   [ 'jason', 'jen', 'vicky' ], 
    #   [ 'jen', 'jason', 'vicky' ], 
    #   [ 'jen', 'vicky', 'jason' ], 
    #   [ 'jason', 'vicky', 'jen' ], 
    #   [ 'vicky', 'jason', 'jen' ], 
    #   [ 'vicky', 'jen', 'jason' ], 
    #   [ 'jason', 'cody', 'vicky' ], 
    #   [ 'cody', 'jason', 'vicky' ], 
    #   [ 'cody', 'vicky', 'jason' ], 
    #   [ 'jason', 'vicky', 'cody' ], 
    #   [ 'vicky', 'jason', 'cody' ], 
    #   [ 'vicky', 'cody', 'jason' ], 
    #   [ 'jen', 'cody', 'vicky' ], 
    #   [ 'cody', 'jen', 'vicky' ], 
    #   [ 'cody', 'vicky', 'jen' ], 
    #   [ 'jen', 'vicky', 'cody' ], 
    #   [ 'vicky', 'jen', 'cody' ], 
    #   [ 'vicky', 'cody', 'jen' ] 
    # ] 
    print(res)
