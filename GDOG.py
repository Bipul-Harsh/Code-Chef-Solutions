for _ in range(int(input())):

    N,K = map(int,input().split())

    max_coins = 0

    for no_people in range(1,K+1):
        coins_left = no_people % N
        if (coins_left > max_coins):
            max_coins = coins_left

    print(max_coins)