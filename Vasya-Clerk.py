# Vasya - Clerk


def tickets(people):
    kitty = 0
    for p in people:
        # do they have exact money?
        if p == 25:
            # great, no need to give change, add money to kitty
            kitty += 25
        else:  # assume they have more than 25
            change_needed = p-25
            # check if there is enough money in the kitty
            if kitty < change_needed:
                return('NO')
            else:  # update the kitty
                kitty += 25
    return("YES")


# tests
print(tickets([25, 50]))
print(tickets([25, 75]))
print(tickets([25, 50, 75]))
print(tickets([25, 50, 75, 25, 50, 100]))
