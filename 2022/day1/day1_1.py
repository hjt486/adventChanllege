def Solver():
    # Space Complexity: O(1) Not counting the storage for input
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day1/input.txt', 'r')
    lines = f.readlines() + ["\n"] # Add a new line for easy process
    accum = 0
    for line in lines:
        if not line or line == "\n":
            accum = 0
        else:
            accum += int(line)
            max_calories = max(max_calories, accum)
    return max_calories

print(Solver())