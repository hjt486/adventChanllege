def SolverMethod():
    # Space Complexity: O(1) only space for parsing and holding stack
    # Time Complexity: O(n)
    f = open('adventChanllege/2022/day5/input.txt', 'r')
    lines = f.readlines()
    stacks = []
    for i in range(len(lines)):
        if not lines[i].strip():
            stacks_count = max([int(x) if x.isdigit() else -1 for x in lines[i-1].split(' ')])
            stacks = [[] for x in range(stacks_count)]
            for j in range(i - 2, -1, -1):
                for k in range(stacks_count):
                    if lines[j][k * 4 + 1].strip():
                        stacks[k].append(lines[j][k * 4 + 1])
            for j in range(i + 1, len(lines)):
                line = lines[j].split(' ')
                count, source, dest = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
                for k in range(count):
                    stacks[dest].append(stacks[source].pop())
            return "".join([x[-1] for x in stacks])

print(SolverMethod())