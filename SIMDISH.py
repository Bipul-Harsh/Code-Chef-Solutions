for _ in range(int(input())):
    print('similar' if len(set(input().split()).intersection(set(input().split())))>=2 else 'dissimilar')