def is_group_anagram(words:list[str])->list[list[str]]:
    result={}
    result_array = []
    for word in words:
        word_map = {}
        for letter in word:
            if letter in word_map:
                word_map[letter]+=1
            else:
                word_map[letter]=1
        result[word]=word_map

    result_word = list(result.keys())
    result_key_len = len(result.keys())
    visited = set()  # to avoid adding same word multiple times

    for i in range(result_key_len):
        word1 = result_word[i]
        if word1 in visited:
            continue

        group = [word1]  # start a new group with this word

        for j in range(i + 1, result_key_len):
            word2 = result_word[j]
            if word2 in visited:
                continue

            if result[word1] == result[word2]:
                group.append(word2)
                visited.add(word2)

        visited.add(word1)
        result_array.append(group)

    return result_array  
    

print(is_group_anagram(['eat','ate','tap']))















































def is_group_anagram(words:list[str])->list[list[str]]:
    result = {}
    for word in words:
        sortedLetterTuple = tuple(sorted(word))
        if sortedLetterTuple in result:
            result[sortedLetterTuple].append(word)
        else:
            result[sortedLetterTuple] = [word]
    return list(result.values())

print(is_group_anagram(['eat','ate','tap']))