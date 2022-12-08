def SolverMethod():
    # Space Complexity: O(n) Worst case if it's a lone single line, O(n) is needed for a set
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day3/input.txt', 'r')
    lines = f.readlines()
    accum = 0
    for line in lines:
        # Use set to find the intersection
        repeated_item = ''.join(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))
        if repeated_item: # if found repeated item
            if repeated_item.upper() == repeated_item: # if is a capital letter
                accum += ord(repeated_item) - ord('A') + 27
            else:
                accum += ord(repeated_item) - ord('a') + 1
    return accum

print(SolverMethod())