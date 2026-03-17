def xor(x, y):
    return (x and not y) or (not x and y)

a, b = map(int, input().split())
print(1 if xor(a == 1, b == 1) else 0)