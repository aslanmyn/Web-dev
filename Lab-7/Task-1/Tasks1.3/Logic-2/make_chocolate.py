def make_chocolate(small, big, goal):
    big_needed = min(big, goal // 5)
    remaining_goal = goal - big_needed * 5
    if small >= remaining_goal:
        return remaining_goal
    return -1

# Test cases
print(make_chocolate(4, 1, 9))   # 4
print(make_chocolate(4, 1, 10))  # -1
print(make_chocolate(4, 1, 7))   # 2
