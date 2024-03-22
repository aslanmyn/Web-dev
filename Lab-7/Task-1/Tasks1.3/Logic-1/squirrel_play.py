def squirrel_play(temperature, is_summer):
    upper_limit = 90 if not is_summer else 100
    return 60 <= temperature <= upper_limit

# Test cases
print(squirrel_play(70, False)) # True
print(squirrel_play(95, False)) # False
print(squirrel_play(95, True))  # True
