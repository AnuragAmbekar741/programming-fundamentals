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

print(roman_to_decimal("XIX"))


def roman_to_decimal2(roman:str)->int:
    roman_hash_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    compound_values = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    result = 0
    skip_next = False
    for i in range(len(roman)):
        if skip_next:
            skip_next = False
            continue
        if i+1<len(roman) and roman[i:i+2] in compound_values:
            result += compound_values[roman[i:i+2]]
            skip_next = True
        else:
            result += roman_hash_map[roman[i]]
    return result

print(roman_to_decimal2("XIX"))

def roman_to_decimal3(roman:str)->int:
    roman_hash_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    compound_values = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    result = 0
    i=0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in compound_values:
            result+=compound_values[roman[i:i+2]]
        else:
            result+=roman_hash_map[roman[i]] 

print(roman_to_decimal3("XIX"))