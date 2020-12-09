for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    i, j = 0, n-1
    completed = True
    last = arr[0]
    k = [1,2,3,4,5,6,7]
    while (i<=j):
        if (arr[i] == arr[j] and arr[i] >= last and arr[i] <= 7 and arr[i] >= 1):
            last = arr[i]
            if (arr[i] in k):
                k.remove(arr[i])
            i += 1
            j -= 1
        else:
            completed = False
            print("no")
            break
    if (completed):
        if len(k) == 0:
            print("yes")
        else:
            print("no")