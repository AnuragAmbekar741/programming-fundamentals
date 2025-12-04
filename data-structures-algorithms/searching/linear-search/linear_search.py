def linear_search(hay_stack:list[int],needle:int):
    for i in range(len(hay_stack)):
        if hay_stack[i] == needle:
            return True
    return False