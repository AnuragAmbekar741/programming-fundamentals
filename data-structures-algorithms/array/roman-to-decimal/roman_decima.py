def roman_to_decimal(roman:str)->int:
    roman_hash_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    
    for i in range(len(roman)):
        if i+1<len(roman) and roman_hash_map[roman[i]]<roman_hash_map[roman[i+1]]:
            result-=roman_hash_map[roman[i]]
        else:
            result+=roman_hash_map[roman[i]]
    return result


