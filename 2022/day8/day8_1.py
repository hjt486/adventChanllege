def SolverMethod():
    # Space Complexity: O(w * h * 5)
    # Time Complexity:  O(w * h * 5) 3-pass
    f = open('adventChanllege/2022/day8/input.txt', 'r')
    lines = f.readlines()
    w, h = len(lines[0].strip()), len(lines)
    matrix = [[[] for i in range(w)]for j in range(h)] # Generate Matrix
    for i in range(h):
        for j in range(w):
            # for each cell, the format is [self value, upper max, lower max, left max, right max]
            if i != 0 and j != 0 and i != h - 1 and j != w - 1:
                # for non-edge cells, init max values to -inf
                matrix[i][j] = [int(lines[i][j]), float("-inf"), float("-inf"), float("-inf"), float("-inf")]
                # for edge cells, init max values to their self values
            else:
                matrix[i][j] = [int(lines[i][j]) for k in range(5)]
    visible_count = w * 2 + h * 2 - 4
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # go through matrix, calculate accum upper max, lower max, left max and right max
            matrix[i][j][1] = max(matrix[i - 1][j][1], matrix[i - 1][j][0]) #upper
            matrix[i][j][3] = max(matrix[i][j - 1][3], matrix[i][j - 1][0]) #left
            matrix[h - i - 1][w - j - 1][2] = max(matrix[h - i][w - j - 1][2], matrix[h - i][w - j - 1][0])#lower
            matrix[h - i - 1][w - j - 1][4] = max(matrix[h - i - 1][w - j][4], matrix[h - i - 1][w - j][0])#right
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # go through matrix again, based calculated max, find visible trees
            if matrix[i][j][0] > matrix[i][j][1] or\
                matrix[i][j][0] > matrix[i][j][2] or\
                matrix[i][j][0] > matrix[i][j][3] or\
                matrix[i][j][0] > matrix[i][j][4]:
                visible_count += 1
    return visible_count

print(SolverMethod())