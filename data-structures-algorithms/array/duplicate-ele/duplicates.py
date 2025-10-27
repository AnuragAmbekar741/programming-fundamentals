array = [1,4,3,5,7]

def has_dups(array):
    hash_map = {}
    for index,value in enumerate(array):
        if value in hash_map:
            return True
        else:
            hash_map[value]=index
    return False


print(has_dups(array))