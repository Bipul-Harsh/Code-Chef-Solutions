for _ in range(int(input())):
    N, M, K = map(int, input().split())
    source_file = {i for i in range(1,N+1)}
    ignored = set(map(int, input().split()))
    tracked = set(map(int, input().split()))
    both = ignored.intersection(tracked)
    ignoredORtracked = ignored.union(tracked)
    not_both = source_file.difference(ignoredORtracked)
    print(len(both), len(not_both))