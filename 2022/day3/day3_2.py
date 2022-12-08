def SolverMethod():
    # Space Complexity: O(n) Worst case if it's a lone single line, O(n) is needed for a set
    # Time Complexity:  O(n)
    f = open('adventChanllege/2022/day3/input.txt', 'r')
    lines = f.readlines()
    accum = 0
    i = 0
    set_ = set()
    while i < len(lines):
        if i % 3 == 0: # if it's the first of the group of 3, set is itself
            set_ = set(lines[i].strip())
        else: # or it's 2nd or 3rd, find intersection
            set_ = set_.intersection(set(lines[i].strip()))
        i += 1
        if i % 3 == 0 or i == len(lines): # if next if new group, found sum and accum it
            repeated_item = ''.join(set_)
            if repeated_item:
                if repeated_item.upper() == repeated_item:
                    accum += ord(repeated_item) - ord('A') + 27
                else:
                    accum += ord(repeated_item) - ord('a') + 1
    return accum

print(SolverMethod())