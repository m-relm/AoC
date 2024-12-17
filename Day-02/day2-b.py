from itertools import pairwise

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

def validate_difference_in_measurement(validation_line: [int]) -> bool:
    iterator = iter(validation_line)
    current_value = next(iterator)
    for next_value in iterator:
        difference = abs(current_value - next_value)
        if 0 < difference > 3:
            print(f"Difference is too high - {current_value} - {next_value} =  {difference}")
            print(f"{validation_line}")
            return True
        current_value = next_value
    print(f"Correct: {validation_line}")
    return False

def remove_invalid_difference(validation_line: [int]):
    id = 0
    iterator = iter(validation_line)
    current_value = next(iterator)
    for next_value in iterator:
        difference = abs(current_value - next_value)
        if 0 < difference > 3:
            validation_line.remove(next_value)
            return validation_line
        current_value = next_value
        id += 1


list_lines = []
with open('./input-1.txt', 'r') as file:
    read_lines = file.readlines()

for line in read_lines:
    line = line.replace('\n', '')
    string_list = line.split(' ')
    list_lines.append(list(map(int, string_list)))

valid_no_dampening = []
valid_with_dampening = []
invalid_failed_dampening = []
invalid_lines = []
value_removed_lines = []
# does_not_all_decrease = []
for list_line in list_lines:
    if all(a < b for a, b in pairwise(list_line)) or all(a > b for a, b in pairwise(list_line)):
        if not validate_difference_in_measurement(list_line):
            valid_no_dampening.append(list_line)
        else:
            adjusted_line = remove_invalid_difference(list_line)
            if not validate_difference_in_measurement(adjusted_line):
                valid_with_dampening.append(adjusted_line)
            else:
                invalid_failed_dampening.append(list_line)
    else:
        if list_line[0] > list_line[1]:  # Decrease
             adjusted_line = remove_invalid_higher_entry(list_line)
        #     if all(a < b for a, b in pairwise(list_line)):
        #         if not validate_difference_in_measurement(adjusted_line):
        #             valid_with_dampening.append(adjusted_line)
            # value_removed_lines.append(adjusted_line)
        elif list_line[0] < list_line[1]:  # Increase
             adjusted_line = remove_invalid_lower_entry(list_line)
        #     if all(a > b for a, b in pairwise(list_line)):
        #         if not validate_difference_in_measurement(adjusted_line):
        #             valid_with_dampening.append(adjusted_line)
            # value_removed_lines.append(adjusted_line)
        else: # same number
             adjusted_line = remove_invalid_lower_entry(list_line)
            # if all(a < b for a, b in pairwise(adjusted_line)) or all(a > b for a, b in pairwise(adjusted_line)):
            #     if not validate_difference_in_measurement(adjusted_line):
            #         valid_with_dampening.append(adjusted_line)
            # value_removed_lines.append(adjusted_line)
            # print("crap")

        # adjusted_line = remove_invalid_entry(list_line)


        invalid_lines.append(list_line)




print(valid_no_dampening)
print(invalid_lines)

