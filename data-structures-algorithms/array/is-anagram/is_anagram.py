def is_anagram(t:str,s:str)->bool:
    if len(t) != len(s):
        return False
    word_one_hash_map = {}
    word_two_hash_map = {} 

    # Count letters in first string
    for letter in t:
        if letter in word_one_hash_map:
            word_one_hash_map[letter] += 1
        else:
            word_one_hash_map[letter] = 1

    # Count letters in second string
    for letter in s:
        if letter in word_two_hash_map:
            word_two_hash_map[letter] += 1
        else:
            word_two_hash_map[letter] = 1
    
    return word_one_hash_map == word_two_hash_map


print(is_anagram("anurag","raaanu"))

def is_anagram2(t:str, s:str) -> bool:
    if len(t) != len(s):
        return False
    
    char_count = [0]*26

    for letter in t:
        char_count[ord(letter)-ord('a')] += 1

    for letter in s:
        char_count[ord(letter)-ord('a')] -= 1

    return all(count == 0 for count in char_count)


print(is_anagram2("anurag","raganu"))