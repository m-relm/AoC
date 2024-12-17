from itertools import product

def open_file():
    with open('./input-1.txt', 'r') as file:
        calibrations = file.readlines()
        calibrations = [calibration.strip().split(":") for calibration in calibrations]
        calibration_values = [int(calibration[0].strip()) for calibration in calibrations]
        equation_values = [[int(val) for val in calibration[1].strip().split(" ")] for calibration in calibrations]
        calibration_dict = []
        for i in range(len(equation_values)):
            calibration_dict.append({
                "equation": equation_values[i],
                "calibration": calibration_values[i]
            })

        return calibration_dict

def generate_combinations(length):
    chars = ['*', '+']
    return [''.join(combination) for combination in product(chars, repeat=length - 1)]


calibration_dict = open_file()

valid_calibrations = 0
calibration_sum = 0
for calibration in calibration_dict:
    calibration_combination = generate_combinations(len(calibration["equation"]))
    for calibration_test in calibration_combination:
        testing_value = calibration["equation"][0]
        for i, op in enumerate(calibration_test):
            # print(calibration["equation"][i + 1])
            if op == '+':
                testing_value += calibration["equation"][i + 1]
            elif op == '*':
                testing_value *= calibration["equation"][i + 1]

        if testing_value == calibration["calibration"]:
            valid_calibrations += 1
            calibration_sum += testing_value
        else:
            print(f"{testing_value} != {calibration['calibration']}")

var = True


# 3254637331:
#
# [* +]
#
# ++++++++++
# **********
# +*++++++++
# +**+++++++
#
#
# 1
# 3
# 32
# 9
# 35
# 6
# 6
# 7
# 1
# 5
# 42