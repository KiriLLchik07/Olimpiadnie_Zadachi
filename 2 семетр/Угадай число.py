def calculate_result(current_value, operation_string, value_x):
    operator, operand = operation_string.split()
    if operand == "x":
        operand = value_x
    if operator == "+":
        return current_value + int(operand)
    if operator == "-":
        return current_value - int(operand)
    if operator == "*":
        return current_value * int(operand)
    if operator == "/":
        return current_value / int(operand)

def main():
    input_lines = open("input_s1_01.txt").readlines()

    for x_value in range(-100, 101):
        result = x_value
        for i in range(1, len(input_lines) - 1):
            result = calculate_result(result, input_lines[i], x_value)
        if result == int(input_lines[len(input_lines) - 1]):
            print(x_value)
            break

if __name__ == "__main__":
    main()
