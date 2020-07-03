"""
Algo: Bottom up Dynamic Programming approach, also keep 'coins' list sorted.


    T[i] - stores min. number of coins, it takes to form i
    'j' is varying from 0 to number of coins
    T[i] is there, when not taking the jth coin
    1 + T[i-coins[j]] is there, when picking jth coin (1 for picking jth coin), then it is T[i- denomination of 'j'], i.e. remaining total
    T[i] = min(T[i], 1+T[i-coins[j]]), update with this, while iterating through all the coins and values(Total) list

    R[] - It is initialised till length of (total+1), considering we are taking all the values from (0,total)
    R[i] - list to get the coin combination, R[i]=j, means jth index coin in coins list, was used to make that total value

T.C. - O(total * len(coins)) - Two for loops, one for (1,total) times, and other for len(coins) times, so time complexity is this
S.C.- O(total), as initializing an array of size (total+1).
"""
def minimumCoins(total, coins):

    # As T[i] represents min. number of coins to form total T[i]
    # So, initialising with T[0] = 0, and taking array length as (total+1)

    T = [float("inf")] * (total+1)
    T[0] = 0  # Number of coins required to make value of 0 is '0'

    # R[] - It is initialised till length of (total+1), considering we are taking all the values from (0,total)
    # # R[i] - list to get the coin combination, R[i]=j, means jth index coin in coins list, was used to make that total value

    R = [-1] * (total+1)

    # Iterating through the coins list
    for j in range(0, len(coins)):

        # Iterating through the T[] list, containing the values from (1 to total)
        for i in range(1, total+1):

            # If 'i' value is more or equal to jth coin denomination value
            if (i >= coins[j]):

                # Updating T[i] with min. of T[j] and 1+T[i-denomination of jth index coin]
                T[i] = min(1+T[i-coins[j]],T[i])
                R[i] = j

    coinCombination(R, coins)

    print ("Minimum Number of Coins required to form total are:")

    if (T[total] > total):
        return -1
    else:
        return T[total]

def coinCombination(R, coins):

    # If last val in R[] list, is equal to -1, means it is not possible to achieve that total
    if (R[len(R)-1] == -1):
        print ("No Solution is possible to achieve that total")
        return

    start = len(R)-1
    print ("Coins used to form total are:")

    # Iterate till start becomes 0, and print coins value at jth index, and subtract that value from start until it becomes 0
    while(start >= 0):
        j = R[start]
        print (coins[j])
        start = start - coins[j]

coins = [1,2,5]
total = 11

# Edge Case
# coins = [2]
# total = 3
print (minimumCoins(total, coins))




