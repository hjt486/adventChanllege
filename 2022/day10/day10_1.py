def SolverMethod():
    # Space Complexity: O(1)
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day10/input.txt', 'r')
    lines = f.readlines()
    clock = 0
    x = 1
    res = 0
    for line in lines:
        line = line.strip().split(' ')
        cycle = 1
        if line[0] == 'addx':
            cycle = 2
        for i in range(cycle):
            clock += 1
            if clock in [20, 60, 100, 140, 180, 220]:
                res += clock * x
        if line[0] == 'addx':
            x += int(line[1])
    return res

print(SolverMethod())