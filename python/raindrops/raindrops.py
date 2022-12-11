FACTOR_STRING = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong',
}

def convert(number):
    result = ''

    for factor_value, str_result in FACTOR_STRING.items():
        result += str_result if number% factor_value == 0 else ''
    
    return result or str(number)
