from operations import add, rest, multiply, divide, power, modulo
def game():
    score = 0
    while True:
        print('======== Menu ========'
            '\n1. Add'
            '\n2. Subtract'
            '\n3. Multiply'
            '\n4. Divide'
            '\n5. Power'
            '\n6. Modulo'
            '\n0. Exit')
        option = int(input('\nChoose an option: '))
        if option == 0:
            break
        num_1 = float(input('Enter first number: '))
        num_2 = float(input('Enter second number: '))
        answer = float(input('Enter your answer: '))
        if option == 1:
            result = add(num_1, num_2)
        elif option == 2:
            result = rest(num_1, num_2)
        elif option == 3:
            result = multiply(num_1, num_2)
        elif option == 4:
            result = divide(num_1, num_2)
        elif option == 5:
            result = power(num_1, num_2)
        elif option == 6:
            result = modulo(num_1, num_2)
        else:
            print('Invalid option. Please try again.')
            continue
        
        if result is not None and result == answer:
            score += 1  # Increase score by 1 for each correct answer
            print('Correct!!')
        else:
            print('Incorrect')
    
    print(f'======== Game Over ========'
        f'\nYour score is {score}'
        '\nKeep going!')

game()
