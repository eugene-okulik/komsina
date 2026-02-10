result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'


def find_number(result_string):
    index_of_number_from_result_string = result_string.index(':') + 2
    number_from_result_string = int(result_string[index_of_number_from_result_string:])
    return number_from_result_string + 10


print(find_number(result_1))
print(find_number(result_2))
print(find_number(result_3))
