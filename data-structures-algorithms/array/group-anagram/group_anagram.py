def is_group_anagram(words:list[str])->list[list[str]]:
    result_map = {}
    result_array = []
    for word in words:
        word_map = {}
        for letter in word:
            if letter in word_map:
                word_map[letter]+=1
            else:
                word_map[letter]=1
        result_map[word] = word_map
    
    total_words = len(words)
    visited_words = set()
    for i in range(total_words):
        word1 = words[i]
        if word1 in visited_words:
            continue
        group = [word1]

        for j in range(i+1,total_words):
            word2 = words[j]
            if word1 in visited_words:
                continue
            if result_map[word1]==result_map[word2]:
                group.append(word2)
                visited_words.add(word2)
        result_array.append(group)
    return result_array

print(is_group_anagram(['act','eat','ate','tac','tap','cat']))

def is_group_anagram(words:list[str])->list[list[str]]:
    result={}
    for word in words:
        sorted_word_tuple = tuple(sorted(word))
        if sorted_word_tuple in result:
            result[sorted_word_tuple].append(word)
        else:
            result[sorted_word_tuple] = [word]
    return list(result.values())

print(is_group_anagram(['act','eat','ate','tac','tap','cat','pat']))
