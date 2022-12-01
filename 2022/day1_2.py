import heapq

def Solver():
    # Space Complexity: O(1)
    # Time Complexity: O(n) Heap take log(3) = 2 to insert or remove, it's constant, so overall O(n)
    f = open('adventChanllege/2022/input.txt', 'r')
    lines = f.readlines() + ["\n"] # Add a new line for easy process
    top3 = [] # heap
    accum = 0
    for line in lines:
        if not line or line == "\n":
            heapq.heappush(top3, accum)
            if len(top3) > 3:
                heapq.heappop(top3)
            accum = 0
        else:
            accum += int(line)
    return sum(top3)

print(Solver())