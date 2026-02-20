# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def choose_operation(func):
    def wrapper(first, second):
        operation = None

        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            if second == 0:
                print('Division is forbidden')
                return None
            else:
                operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)

    return wrapper


@choose_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    return None


number1 = int(input('Input first number: '))
number2 = int(input('Input second number: '))

result = calc(number1, number2)
print(result)
