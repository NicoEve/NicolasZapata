def add(num_1, num_2):
    result = num_1 + num_2
    print(f'{num_1} + {num_2} is equal to {result}')
    return result

def rest(num_1, num_2):
    result = num_1 - num_2
    print(f'{num_1} - {num_2} is equal to {result}')
    return result

def multiply(num_1, num_2):
    result = num_1 * num_2
    print(f'{num_1} * {num_2} is equal to {result}')
    return result

def divide(num_1, num_2):
    if num_2 == 0:
        print("Error: Division by zero!")
        return None
    result = num_1 / num_2
    print(f'{num_1} / {num_2} is equal to {result}')
    return result

def power(num_1, num_2):
    result = num_1 ** num_2
    print(f'{num_1} ^ {num_2} is equal to {result}')
    return result

def modulo(num_1, num_2):
    if num_2 == 0:
        print("Error: Division by zero!")
        return None
    result = num_1 % num_2
    print(f'{num_1} % {num_2} is equal to {result}')
    return result