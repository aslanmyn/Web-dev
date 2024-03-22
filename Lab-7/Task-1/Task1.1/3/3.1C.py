a, b = map(int, input().split())

found = False

for num in range(a, b + 1):
    if int(num ** 0.5) ** 2 == num:
        print(num, end=" ")
        found = True

if not found:
    pass
