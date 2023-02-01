def SolverMethod():
    # Space Complexity: O(1)
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day10/input.txt', 'r')
    lines = f.readlines()
    clock = 0
    x = 1
    res = ""
    for line in lines:
        line = line.strip().split(' ')
        cycle = 1
        if line[0] == 'addx':
            cycle = 2
        for i in range(cycle):
            clock += 1
            if (clock) % 40 - 1 in [x-1, x, x+1]:
                res += '#'
            else:
                res += '.'
            if clock % 40 == 0:
                res += '\n' 
        if line[0] == 'addx':
            x += int(line[1])
    return res

print(SolverMethod())