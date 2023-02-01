def SolverMethod():
    # Space Complexity: O(m) every coordinates is not repeated
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day9/input.txt', 'r')
    lines = f.readlines()
    dir_coords = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    t_set = {(0,0)} # to count only
    def getDirection(x, y): # based on x and y to return where to move
        res = [0, 0]
        if x > 0: res[0] = 1
        elif x < 0: res[0] = -1
        if y > 0: res[1] = 1
        elif y < 0: res[1] = -1
        return res
    for line in lines:
        line = line.strip().split(' ')
        dir, steps = line[0], int(line[1])
        for k in range(steps):
            rope[0] = [x + y for (x, y) in zip(rope[0], dir_coords[dir])]
            for l in range(1, len(rope)):
                pre = rope[l - 1]
                cur = rope[l]
                dist = [pre[0] - cur[0], pre[1] - cur[1]]
                true_dist = dist[0]**2 + dist[1]**2
                x, y = getDirection(dist[0], dist[1])
                if true_dist >= 4: # if a^2 + b^2 >= 4, means not touching
                    rope[l][0] += x # Move accordingly
                    rope[l][1] += y
            t_set.add(tuple(rope[-1]))
        
    return len(t_set)

print(SolverMethod())
