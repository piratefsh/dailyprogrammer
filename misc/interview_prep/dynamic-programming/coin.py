import sys

def min_coins(coins, target):
    # set min[i] to infinity for all of i
    mins = [sys.maxsize] * (target + 1)

    # min[0] = 0
    mins[0] = 0

    # for i = 1 to target
    #   for j = 0 to N - 1
    for cents in range(target+1):
        for coin in coins:
            # if coin is less than target and if adding another coin
            # to the min coins one before is less than currently, update
            if coin <= cents and mins[cents-coin] + 1 < mins[cents]:
                mins[cents] = mins[cents-coin] + 1

    return mins[target]

def min_coins_recursive(coins, target):
    if target < 0:
        return sys.maxsize
    elif target == 0:
        return 0
    else:
        possiblities = [min_coins_recursive(coins, target-coins[i]) for i in range(len(coins))]
        min_poss = min(possiblities) if len(possiblities) > 0 else 0
        return 1 + min_poss

def test():
    assert min_coins([1, 3, 5], 11) == 3
    assert min_coins_recursive([1, 3, 5], 11) == 3
    print('tests pass')