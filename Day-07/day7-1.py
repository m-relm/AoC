from itertools import product

# Function to generate all combinations of + and *
def generate_combinations(chars, length):
    return [''.join(combination) for combination in product(chars, repeat=length)]

# Function to evaluate the expression with given operators
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '|':
            result = int(str(result) + str(numbers[i + 1]))
    return result

# Function to find matching expression
def find_matching_expression(target, numbers, chars=['+', '*', '|']):
    operator_combinations = generate_combinations(chars, len(numbers) - 1)
    for ops in operator_combinations:
        if evaluate_expression(numbers, ops) == target:
            expression = f"{numbers[0]}"
            for i, op in enumerate(ops):
                expression += f" {op} {numbers[i + 1]}"
            return expression
    return None  # No matching expression found


def open_file():
    with open('./input-1.txt', 'r') as file:
        calibrations = file.readlines()
        calibrations = [calibration.strip().split(":") for calibration in calibrations]
        calibration_values = [calibration[0].strip() for calibration in calibrations]
        equation_values = [calibration[1].strip().split(" ") for calibration in calibrations]
        calibration_dict = []
        for i in range(len(equation_values)):
            calibration_dict.append({
                "equation": equation_values[i],
                "calibration": calibration_values[i]
            })

        return calibration_dict

# Compute matches
results = {}
calibration_dict = open_file()
for calibration in calibration_dict:
    print(f"Validating {calibration['calibration']}")
    results[calibration["calibration"]] = find_matching_expression(int(calibration["calibration"]), list(map(int, calibration["equation"])))

total_valid = 0
for result in results:
    if results[result] is not None:
        total_valid += int(result)

# for target, numbers in calibration_dict.items():
#     results[target] = find_matching_expression(target, numbers)

var = True