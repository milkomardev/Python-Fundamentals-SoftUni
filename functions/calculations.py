def calculator(operator, num1, num2):
    if command == 'multiply':
        result = num1 * num2
        return result
    if command == 'divide':
        result = num1 // num2
        return result
    if command == 'add':
        result = num1 + num2
        return result
    if command == 'subtract':
        result = num1 - num2
        return result


command = input()
number1 = int(input())
number2 = int(input())

print(calculator(command, number1, number2))
