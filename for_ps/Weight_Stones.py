
def lastStoneWeight(stones):
    while len(stones) >= 2:
        stones.sort()
        
        s1 = stones[-1]
        s2 = stones[-2]

        stones.remove(s1)
        stones.remove(s2)

        if s1 > s2:
            stones.append(s1-s2)

    if len(stones) == 1:
        return stones.pop()
    elif len(stones) <= 1:
        return 0
    else:
        return stones
        
lst= list(map(int,input().split(",")))


