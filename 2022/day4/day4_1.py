def SolverMethod():
    # Space Complexity: O(1)
    # Time Complexity: O(n)
    f = open('adventChanllege/2022/day4/input.txt', 'r')
    lines = f.readlines()
    count = 0
    for line in lines:
        line = line.strip().split(',')
        a, b = int(line[0].split('-')[0]), int(line[0].split('-')[1])
        c, d = int(line[1].split('-')[0]), int(line[1].split('-')[1])
        if c >= a and d <= b or a >= c and b <= d:
            count += 1 
    return count

print(SolverMethod())