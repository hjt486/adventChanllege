def SolverMethod():
    # Space Complexity: O(m) every coordinates is not repeated
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day9/input.txt', 'r')
    lines = f.readlines()
    dir_coords = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    h, s = [[0, 0], [0, 0]], [0, 0] # head has pre, and cur
    t_set = {(0,0)} # to count only
    for line in lines:
        line = line.strip().split(' ')
        dir, dist = line[0], int(line[1])
        for k in range(dist):
            h[0], h[1] = h[1], [x + y for (x, y) in zip(h[1], dir_coords[dir])]
            s_near_h = False
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if s == [h[1][0] + i, h[1][1] + j]:
                        s_near_h = True
            if not s_near_h:
                s[0], s[1] = h[0][0], h[0][1]
            t_set.add(tuple(s))
    return len(t_set)

print(SolverMethod())

