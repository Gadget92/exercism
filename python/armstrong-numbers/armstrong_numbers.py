def is_armstrong(number):
    in_val = number
    numbers = []
    while in_val > 0:
        numbers.append(in_val % 10)
        in_val = in_val // 10

    total = sum(i ** len(numbers) for i in numbers)
    
    return total == number