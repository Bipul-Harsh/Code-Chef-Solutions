# cook your dish here
for _ in range(int(input())):
    n = input()
    s = input()
    vertical_progress = ['U', 'D']
    horizontal_progress = ['L', 'R']
    (x,y) = (0,0)
    opr = {'U':1, 'D': -1, 'L': -1, 'R': 1}
    axis = -1 # 0 horizontal, 1 = vertical
    for step in s:
        if step in vertical_progress and axis != 1:
            y += opr[step]
            axis = 1
        elif step in horizontal_progress and axis != 0:
            x += opr[step]
            axis = 0
    print(x, y)