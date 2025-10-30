def group_anagram(strs:list[str])->list[list[str]]:
    result = {} 
    for word in strs:
        word_hash_map = {}
        for letter in word:
            if letter in word_hash_map:
                word_hash_map[letter]+=1
            else:
                word_hash_map[letter]=1

        key = tuple(sorted(word_hash_map.items()))
        
        # Add word to the group with this key
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    
    # Return just the grouped words (without the keys)
    return list(result.values())

# Test it
print(group_anagram(["eat", "tea", "tan"]))