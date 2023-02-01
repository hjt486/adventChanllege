def SolverMethod():
    # Space Complexity: O(1)
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day11/input.txt', 'r')
    lines = f.readlines() + ['\n']
    index = 0
    data = []
    monkeys = []
    def getNewWorryLevel(old, formula):
        a = old
        b = old
        if formula[2].isdigit():
            b = int(formula[2])
        if formula[1] == '+':
            return a + b
        else:
            return a * b
    for line in lines:
        if index % 7 == 1:
            data.append([int(x) for x in line.strip().split(':')[1].strip().split(',')])
        elif index % 7 == 2:
            data.append(line.strip().split(':')[1].strip().split('=')[1].strip().split(' '))
        elif index % 7 == 3:
            data.append(int(line.split(':')[1].strip().split(' ')[2]))
        elif index % 7 == 4 or index % 7 == 5:
            data.append(int(line.split(':')[1].strip().split(' ')[3]))
        elif index % 7 == 6:
            monkeys.append(data + [0])
            data = []
        index += 1
    sort = []
    ROUND = 20
    for i in range(ROUND):
        for j in range(len(monkeys)):
            for k in range(len(monkeys[j][0])):
                monkeys[j][5] += 1
                oldWorryLevel = monkeys[j][0][k]
                NewWorryLevel = getNewWorryLevel(oldWorryLevel, monkeys[j][1])
                NewWorryLevel //= 3
                if NewWorryLevel % monkeys[j][2] == 0:
                    monkeys[monkeys[j][3]][0].append(NewWorryLevel)
                else:
                    monkeys[monkeys[j][4]][0].append(NewWorryLevel)
            monkeys[j][0] = []
            if i == ROUND - 1:
                sort.append(monkeys[j][-1])
    sort = sorted(sort, reverse = True)[:2]
    return sort[0] * sort[1]

print(SolverMethod())