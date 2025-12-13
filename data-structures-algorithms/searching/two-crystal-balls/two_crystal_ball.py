import math

def two_crystal_balls(breaks:list[bool])->int:
    jump = math.floor(math.sqrt(len(breaks)))
    i = jump
    for i in range(jump,len(breaks),jump):
        if breaks[i]:
            break
    i -= jump
    for j in range(i,i+jump):
        if breaks[j]:
            return j
    return -1

print(two_crystal_balls([False,False,False,False,False,False,False,False,False,False,True]))