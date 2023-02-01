# Try to use non-simulation method, but failed, the result is not correct, will look at it later

def SolverMethod():
    # Space Complexity: O(w * h * 5)
    # Time Complexity:  O(w * h * 5) 3-pass
    f = open('adventChanllege/2022/day9/input.txt', 'r')
    lines = f.readlines()
    dir_pair = {'U':'D', 'D':'U', 'L': 'R', 'R': 'L', None: None}
    dir_coords = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    pre_dir = None
    H = [0, 0]
    t_set = {(0,0)}
    for line in lines:
        line = line.strip().split(' ')
        dir, dist = line[0], int(line[1])
        print(dir, dist)
        count = dist
        if dir_pair[pre_dir] == dir:
            count -= 1
        if dir != pre_dir:
            count -= 1
        for i in range(dist):
            H = [x + y for (x, y) in zip(H, dir_coords[dir])]
        T = [x for x in H]
        for j in range(count):
            T = [x + y for (x, y) in zip(T, dir_coords[dir_pair[dir]])]
            t_set.add(tuple(T))
            print(T)
        if dist != 1:
            pre_dir = dir
    return len(t_set)

print(SolverMethod())
