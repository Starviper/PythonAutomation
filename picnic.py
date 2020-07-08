allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'sandwiches': 3, 'apples': 2}, 'Carol': {'cups': 3, 'plates': 3}}

def totalBrought(guests, item):
    numBrought=0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Number of things beight brought:')
print(' - Apples     ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups       ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes      ' + str(totalBrought(allGuests, 'cakes')))
print(' - sandwiches ' + str(totalBrought(allGuests, 'sandwiches')))
print(' - plates     ' + str(totalBrought(allGuests, 'plates')))
