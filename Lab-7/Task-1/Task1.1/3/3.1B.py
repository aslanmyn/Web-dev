a, b, c, d = map(int, input().split())

found = False

for num in range(a, b + 1):
    if num % d == c:
        print(num, end=" ")
        found = True


if not found:
    pass
