def SolverMethod():
    # Space Complexity: O(1) 26 letters is consider constant
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day6/input.txt', 'r')
    data = f.readlines()[0]
    dict = {}
    count = 0
    for i in range(len(data)):
        count += 1
        c = data[i]
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
        if i >= 4:
            pre_c = data[i - 4]
            if pre_c in dict:
                dict[pre_c] -= 1
                if dict[pre_c] == 0:
                    dict.pop(pre_c)
        if len(dict) >= 4:
            return count
print(SolverMethod())