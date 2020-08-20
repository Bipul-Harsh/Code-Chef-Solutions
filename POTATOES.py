from sys import stdin, stdout
int_input = lambda: int(stdin.readline().strip())
int_list = lambda: list(map(int, stdin.readline().strip().split()))
for _ in range(int_input()):
    x, y = int_list()
    for i in range(x + y + 1, 2050):
        if not (i == 1 or any(i % x == 0 for x in range(2, int(i ** 0.5) + 1))):
            stdout.write(f"{i - (x + y) }\n")
            break