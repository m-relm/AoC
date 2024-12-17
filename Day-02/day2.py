# Open the file and read lines
from itertools import pairwise
from typing import Optional, Tuple
from collections import defaultdict

def validate_ascending_or_descending(validation_line: [int]) -> Tuple[Optional[int], bool]:
    if validation_line == [37, 39, 36, 30, 24]:
        var = True
    if all(a < b for a, b in pairwise(validation_line)) or all(a > b for a, b in pairwise(validation_line)):
        return validation_line, False
    else:
        if all(a < b for a, b in pairwise(validation_line)):
            dampened_line = remove_invalid_lower_entry(validation_line)
            if all(a < b for a, b in pairwise(dampened_line)):
                return dampened_line, True
            else:
                print(f"remove {validation_line}")
                return None, True
        elif all(a > b for a, b in pairwise(validation_line)):
            dampened_line = remove_invalid_higher_entry(validation_line)
            if all(a > b for a, b in pairwise(dampened_line)):
                return dampened_line, True
            else:
                print(f"remove {validation_line}")
                return None, True


    # else: # Something goes down
    #     dampened_line = remove_invalid_lower_entry(validation_line)
    #     if all(a < b for a, b in pairwise(dampened_line)):
    #         return dampened_line, True
    #     else:
    #         return None, True
    #
    # if :
    #     return validation_line, False
    # else: # Something goes up
    #     dampened_line = remove_invalid_higher_entry(validation_line)
    #     if all(a > b for a, b in pairwise(dampened_line)):
    #         return dampened_line, True
    #     else:
    #         return None, True
    #
    print(f"remove {validation_line}")
    return None, True

def remove_invalid_lower_entry(validation_line: [int]):
    iterator = iter(list_line)
    current_value = next(iterator)
    for next_value in iterator:
        if next_value <= current_value:
            validation_line.remove(next_value)
            break
        current_value = next_value

    return validation_line

def remove_invalid_higher_entry(validation_line: [int]):
    iterator = iter(list_line)
    current_value = next(iterator)
    for next_value in iterator:
        if next_value >= current_value:
            validation_line.remove(next_value)
            break
        current_value = next_value

    return validation_line

def validate_difference_in_measurement(validation_line: dict) -> bool:
    iterator = iter(validation_line['data'])
    current_value = next(iterator)
    for next_value in iterator:
        difference = abs(current_value - next_value)
        if 0 < difference > 3:
            print(f"Difference is too high - {current_value} - {next_value} =  {difference}")
            print(f"{validation_line['data']}")
            return True
        current_value = next_value
    print(f"Correct: {validation_line['data']}")
    return False

def remove_invalid_difference(validation_line: dict):
    id = 0
    iterator = iter(validation_line['data'])
    current_value = next(iterator)
    for next_value in iterator:
        difference = abs(current_value - next_value)
        if 0 < difference > 3:
            validation_line['data'].remove(next_value)
            return validation_line
        current_value = next_value
        id += 1
    return False

    # for comparison_line in cleaned_list:
    #     print(comparison_line)
    #     iterator = iter(comparison_line)
    #     current_value = next(iterator)
    #     valid_line = True
    #     for next_value in iterator:
    #         difference = abs(current_value - next_value)
    #         print(difference)
    #         if 0 < difference > 3:
    #             valid_line = False
    #         current_value = next_value
    #     if valid_line:
    #         total_valid_lines += 1
    #
    # pass


list_lines = []
with open('./input-1.txt', 'r') as file:
    read_lines = file.readlines()

for line in read_lines:
    line = line.replace('\n', '')
    string_list = line.split(' ')
    list_lines.append(list(map(int, string_list)))

cleaned_list = [dict]
for list_line in list_lines:
    valid_line, dampened = validate_ascending_or_descending(list_line)
    if valid_line:
        cleaned_list.append(
            {
                "data": valid_line,
                "dampened": dampened,
            }
        )

    # if all(a < b for a, b in pairwise(list_line)) or all(a > b for a, b in pairwise(list_line)):

    # else:

cleaned_list.pop(0)


total_valid_lines = 0
for comparison_line in cleaned_list:
    dampen_entry = validate_difference_in_measurement(comparison_line)
    if dampen_entry:
        if not comparison_line['dampened']: # Are we double triggering dampening?
            comparison_line['dampened'] = True
            comparison_line = remove_invalid_difference(comparison_line)
            dampen_entry = validate_difference_in_measurement(comparison_line)
            if not dampen_entry:
                total_valid_lines += 1
    else:
        total_valid_lines += 1


    # print(comparison_line)
    # iterator = iter(comparison_line['data'])
    # current_value = next(iterator)
    # valid_line = True
    # for next_value in iterator:
    #     difference = abs(current_value - next_value)
    #     #print(difference)
    #     if 0 < difference > 3:
    #         valid_line = False
    #     current_value = next_value
    # if valid_line:
    #     total_valid_lines += 1
    # # exit(0)

print(total_valid_lines)



#
# total_valid_lines = 0
# for list_line in cleaned_list:
#     line_valid = False
#     iterator = iter(list_line)
#     current_value = next(iterator)
#     for next_value in iterator:
#         difference = abs(current_value - next_value)
#         if 1 >= difference >= 3:
#             valid_lines[-1] = True
#         else:
#             valid_lines[-1] = False
#             break
#         current_value = next_value
#     if line_valid:
#         total_valid_lines += 1
#
# print(total_valid_lines)
#
# print('Mark')
# line_id = 0
# for list_line in cleaned_list:
#     for i in range(len(list_line)):
#         first = list_line[i]
#         second = list_line[i + 1]
#         difference = abs(second - first)
#
#         if 1 >= difference >= 3:
#             valid_lines[line_id] = False
#             break
#         else:
#             valid_lines[line_id] = True
#     line_id += 1
#     #
#     #
#     # first_value = list_line[0]
#     # second_value = list_line[1]
#     # is_increasing = first_value < second_value
#     # for i in range(len(list_line)):
#     #     if is_increasing:
#     #         if list_line[i] < list_line[i+1]:
#     #             first = list_line[i]
#     #             second = list_line[i+1]
#     #             difference = second - first
#     #             # print(difference)
#     #
#     #         else:
#     #             valid_lines[line_id] = False
#     #             break
#     #
#     #
#     #     else:
#     #         if list_line[i] > list_line[i+1]:
#     #             first = list_line[i]
#     #             second = list_line[i+1]
#     #             difference = first - second
#     #             # print(difference)
#     #             if 1 >= difference >= 3:
#     #                 valid_lines[line_id] = False
#     #                 break
#     #             else:
#     #                 valid_lines[line_id] = True
#     #         else:
#     #             valid_lines[line_id] = False
#     #             break
#     #     if i+1 == len(list_line):
#     #         break
#     # valid_lines[line_id] = True
#
#
# print('Mark2')
#
# total_safe = 0
# for valid_line in valid_lines:
#     if valid_line:
#         total_safe += 1
#
# print(total_safe)


[39, 42, 45, 43, 44]