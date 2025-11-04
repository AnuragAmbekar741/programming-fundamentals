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







