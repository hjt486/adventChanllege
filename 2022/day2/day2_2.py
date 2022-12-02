def Solver():
    # Space Complexity: O(1)
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day2/input.txt', 'r')
    lines = f.readlines()
    score_dict = {'A': 1, 'B': 2, 'C':3} # A for rock +1 score, B for paper +1, C for scissors +1
    action_to_weight = {'A': 0, 'B': 1, 'C': 2} # Assign weight to each action
    weight_to_action = ['A', 'B', 'C'] # weight 0 is A, weight 1 is B, weight 2 is C
    total_score = 0
    for line in lines:
        op, pl_exp = [x.strip() for x in line.split(" ")] # get opponent's action and player's expectation
        pl_weight = 0
        if pl_exp == 'X':
            pl_weight = (action_to_weight[op] - 1) % 3
            # loose do nothing to total_score
        elif pl_exp == 'Y':
            pl_weight = action_to_weight[op]
            total_score += 3 # draw
        else:
            pl_weight = (action_to_weight[op] + 1) % 3
            total_score += 6 # win
        pl = weight_to_action[pl_weight] # get player action's weight
        total_score += score_dict[pl] # add action's score to total score
    return total_score

print(Solver())
