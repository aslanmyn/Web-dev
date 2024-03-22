N = int(input())

is_power_of_two = True

while N > 1:
    if N % 2 != 0:
        is_power_of_two = False
        break
    N //= 2

if is_power_of_two:
    print("YES")
else:
    print("NO")
