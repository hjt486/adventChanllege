def SolverMethod():
    # Space Complexity: O(w * h * 5) + (2 * 10 * w) + (2 * 10 * h) matrix + u, r, l, r
    # Time Complexity:  O(w * h * 10) 3-pass
    f = open('adventChanllege/2022/day8/input.txt', 'r')
    lines = f.readlines()
    w, h = len(lines[0].strip()), len(lines)
    # Generate main matrix, the format is [value, closest same or higher tree's index in upper direction, ... lower, ... left, ...right]
    matrix = [[[] for i in range(w)]for j in range(h)]
    '''
    Generate upper, lower, left, right matrices to hold the highest (lowest) index for each number,
    use given example:
    30373
    25512
    65332
    33549
    35390
    u[2][5] records the highest index for number 5 in column 2, which will be index 3
    d[2][5] records the lowest index for number 5 in column 2, which will be index 1

    Initialize forward direction (upper, left) to 0, backward direction(lower, right) to w-1 and h-1.
    '''
    u, d, l, r = [[0] * 10 for i in range(w)], [[h-1] * 10 for i in range(w)], [[0] * 10 for i in range(h)], [[w - 1] * 10 for i in range(h)]
    for i in range(h):
        for j in range(w):
            # Same init like udlr matrix
            matrix[i][j] = [int(lines[i][j]), 0, h-1, 0, w-1]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            for k in range(9, -1, -1): # tree height is limited to [0, 9]
                if k >= matrix[i][j][0]:
                    # Forward direction, Find lowest tree height that will block view from current tree, update the index
                    matrix[i][j][1] = max(u[j][k], matrix[i][j][1])
                    matrix[i][j][3] = max(l[i][k], matrix[i][j][3])
                if k >= matrix[h - i - 1][w - j - 1][0]:
                    # Same for backward direction
                    matrix[h - i - 1][w - j - 1][2] = min(d[w - j - 1][k], matrix[h - i - 1][w - j - 1][2])
                    matrix[h - i - 1][w - j - 1][4] = min(r[h - i - 1][k], matrix[h - i - 1][w - j - 1][4])
            # Update all forward and backward matrics (index)
            u[j][matrix[i][j][0]] = i
            d[w - j - 1][matrix[h - i - 1][w - j - 1][0]] = h - i - 1
            l[i][matrix[i][j][0]] = j
            r[h - i - 1][matrix[h - i - 1][w - j - 1][0]] = w - j - 1
    max_score = float("-inf")
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # Go through matrix again and calcualte the score
            max_score = max(max_score, (i - matrix[i][j][1]) *  (matrix[i][j][2] - i) *  (j - matrix[i][j][3]) *  (matrix[i][j][4] - j))
    return max_score

print(SolverMethod())