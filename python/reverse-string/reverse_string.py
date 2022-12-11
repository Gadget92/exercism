def reverse(text):
    if isinstance(text, str):
        return text[::-1]
    else:
        raise ValueError('input data not a string')

def reverse2(text):
    if isinstance(text, str):
        return "".join(reversed(text))
    else:
        raise ValueError('input data not a string')
