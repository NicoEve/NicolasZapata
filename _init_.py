from operations import power

def game():
    score = 0
    while True:
        print('======== Menu ========'
            '\n1. Power'
            '\n0. Exit')
        option = int(input('\nChoose an option: '))
        if option == 0:
            break
        num_1 = int(input('Enter base number: '))
        num_2 = int(input('Enter exponent number: '))
        answer = int(input('Enter your answer: '))
        if option == 1:
            result = power(num_1, num_2)
            if result == answer:
                score += 4  
                print('Correct!!')
            else:
                print('Incorrect')
    print(f'======== Game Over ========'
        f'\nYour score is {score}'
        '\nKeep going!')

game()