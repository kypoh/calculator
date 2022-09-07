running = True
while running:
    first_number = input('choose a number\n')
    first_number = float(first_number)

    second_number = input('choose another number\n')
    second_number = float(second_number)


    expression = input('do you want to add, subtract, multiply or divide\n')

    if expression == 'x':
        running = False

    answer = 0
    operation = ''

    if expression == 'add':
        answer = first_number + second_number
        operation = 'sum'


    elif expression == 'subtract':
        answer = first_number - second_number
        operation = 'minus'

    elif expression == 'multiply':
        answer = first_number * second_number
        operation = 'product'

    elif expression == 'divide':
        answer = first_number / second_number
        operation = 'divide'

    else:
        print('stupid')

    print(f'The {operation} is {answer}')


# number:
# number:
#
# sum:
