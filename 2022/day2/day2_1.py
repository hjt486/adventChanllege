def Solver():
    # Space Complexity: O(1)
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day2/input.txt', 'r')
    lines = f.readlines()
    score_dict = {'X': 1, 'Y': 2, 'Z':3}
    weights = {'X': 0, 'Y': 1, 'Z':2, 'A': 0, 'B': 1, 'C':2} # Assign weight to each action
    total_score = 0
    for line in lines:
        op, pl = [x.strip() for x in line.split(" ")] # get opponent's action and player's action
        total_score += score_dict[pl]
        if weights[op] == weights[pl]: # if draw +3
            total_score += 3
        elif (weights[op] + 1) % 3 == weights[pl]: # if win +6
            total_score += 6
        # if loose, do nothing
    return total_score

print(Solver())