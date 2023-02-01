def ASCIIadd(num1, num2):
        c = 0
        res = ''
        num1, num2 = num1.strip()[::-1], num2.strip()[::-1]
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        for i in range(len(num1)):
            a = 0
            b = 0
            if i < len(num1):
                a = int(num1[i])
            if i < len(num2):
                b = int(num2[i])
            r = a + b + c
            res += str(r % 10)
            c = r // 10
        if c:
            res += str(c)
        return res[::-1]

def ASCIImultiply(num1, num2):
    num1, num2 = num1.strip()[::-1], num2.strip()[::-1]
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    accum = "0"
    for i in range(len(num1)):
        temp_res = "".join(["0" for x in range(i)])
        a = int(num1[i])
        c = 0
        for j in range(len(num2)):
            b = int(num2[j])
            r = a * b + c
            temp_res += str(r % 10)
            c = r // 10
        if c:
            temp_res += str(c)
        accum = ASCIIadd(accum, temp_res)
    return accum[::-1]

def ASCIImod(num1, num2):
    num1 = num1.strip()
    res = 0
    for i in range(len(num1)):
        res = (res * 10 + int(num1[i])) % num2
    return res

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
        if formula[2] != "old":
            b = formula[2]
        if formula[1] == '+':
            return ASCIIadd(a, b)
        else:
            return ASCIImultiply(a, b)

    for line in lines:
        if index % 7 == 1:
            data.append([x for x in line.strip().split(':')[1].strip().split(',')])
        elif index % 7 == 2:
            data.append(line.strip().split(':')[1].strip().split('=')[1].strip().split(' '))
        elif index % 7 == 3:
            data.append((line.split(':')[1].strip().split(' ')[2]))
        elif index % 7 == 4 or index % 7 == 5:
            data.append(int(line.split(':')[1].strip().split(' ')[3]))
        elif index % 7 == 6:
            monkeys.append(data + [0])
            data = []
        index += 1
    sort = []
    ROUND = 1000
    for i in range(ROUND):
        for j in range(len(monkeys)):
            for k in range(len(monkeys[j][0])):
                monkeys[j][5] += 1
                oldWorryLevel = monkeys[j][0][k]
                NewWorryLevel = getNewWorryLevel(oldWorryLevel, monkeys[j][1])
                print("-----")
                print(NewWorryLevel)
                if ASCIImod(NewWorryLevel, int(monkeys[j][2])) == 0:
                    monkeys[monkeys[j][3]][0].append(NewWorryLevel)
                else:
                    monkeys[monkeys[j][4]][0].append(NewWorryLevel)
            monkeys[j][0] = []
            if i + 1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
                pass
                print(monkeys[j][-1])
            if i == ROUND - 1:
                sort.append(monkeys[j][-1])
        if i + 1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            pass
            print("-----")
    sort = sorted(sort, reverse = True)[:2]
    #print(sort)
    return sort[0] * sort[1]

print(SolverMethod())