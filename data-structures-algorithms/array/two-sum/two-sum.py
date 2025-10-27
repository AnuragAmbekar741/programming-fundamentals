array = [2, 7, 11, 15,3,0,3,40]
target = 55

hash_map = {}

for index,value in enumerate(array):
    complement = target - value

    if complement in hash_map:
        print(f"Found! Indices:[{hash_map[complement],index}]")
        print(f"Found! values:[{complement,{value}}]")

    hash_map[value] = index

print(f"Hash map: {hash_map}")