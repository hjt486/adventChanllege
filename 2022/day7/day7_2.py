def SolverMethod():
    # Space Complexity: O(1) only space for parsing and holding stack
    # Time Complexity: O(n)
    f = open('adventChanllege/2022/day7/input.txt', 'r')
    lines = f.readlines()
    dict = {"/": {'size': 0, '..': None}}
    i = 0
    cur = dict
    while i < len(lines):
        line = lines[i].strip().split(' ')
        if line[0] == "$":
            if line[1] == "cd":
                cur = cur[line[2]]
            elif line[1] == "ls":
                j = i + 1
                while j < len(lines):
                    new_line = lines[j].strip().split(' ')
                    if new_line[0] == '$':
                        break
                    if new_line[0] == 'dir' and new_line[1] not in cur:
                        cur[new_line[1]] = {'..' : cur, 'size' : 0}
                    else:
                        cur['size'] += int(new_line[0])
                    j += 1
        i += 1
    
    def cal_size(folder):
        for key, dir in folder.items():
            if key != 'size' and key != '..':
                folder['size'] += cal_size(dir)
        return folder['size']

    cal_size(dict['/'])

    res = [float("inf")]
    
    def find_folder(folder):
        for key, dir in folder.items():
            if key != 'size' and key != '..':
                find_folder(dir)
                
        if 70000000 - dict['/']['size'] + folder['size'] >= 30000000:
            res[0] = min(folder['size'], res[0])

    find_folder(dict['/'])
    return res[0]

print(SolverMethod())