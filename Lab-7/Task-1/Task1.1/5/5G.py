N = int(input())
array = list(map(int, input().split()))


end_index = N - 1


for i in range(N // 2):

    array[i], array[end_index] = array[end_index], array[i]

    end_index -= 1


print(*array)
