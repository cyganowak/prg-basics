###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    result = 0
    while number > 0:
        digit = number % 10
        result += digit
        number = number // 10
    return result

any_number = int(input('Enter integer number: '))
number = abs(any_number)
result = sum_digits(number)
print(f'The sum of the digits in the number {any_number} is {result}')
