from itertools import pairwise

def validate_difference_in_measurement(validation_line: [int]) -> bool:
    iterator = iter(validation_line)
    current_value = next(iterator)
    for next_value in iterator:
        difference = abs(current_value - next_value)
        if 1 < difference > 3:
            # print(f"Difference is too high - {current_value} - {next_value} =  {difference}")
            # print(f"{validation_line}")
            return True
        current_value = next_value
    # print(f"Correct: {validation_line}")
    return False

list_lines = []
with open('./input-1.txt', 'r') as file:
    read_lines = file.readlines()

for line in read_lines:
    line = line.replace('\n', '')
    string_list = line.split(' ')
    list_lines.append(list(map(int, string_list)))

valid_lines = []
dampened_valid_lines = []
for list_line in list_lines:
    #loop this twice, if it's true on the second run then we're good?

    problem_dampened = False
    failed_line = False
    for i in range(2):
        if not failed_line:
            if len(list_line) != len(set(list_line)): #Is there a Duplicate
                if problem_dampened:
                    print(f"Two failures detected {list_line}")
                    failed_line = True
                else:
                    iterator = iter(list_line)
                    current_value = next(iterator)
                    for next_value in iterator:
                        if next_value == current_value:
                            list_line.remove(next_value)
                            break
                        current_value = next_value

                    problem_dampened = True
            if list_line[0] < list_line[1]:
                if not all(a < b for a, b in pairwise(list_line)): #Does everything Increase?
                    if problem_dampened and not failed_line:
                        print(f"Two failures detected {list_line}")
                        failed_line = True
                    else:
                        iterator = iter(list_line)
                        current_value = next(iterator)
                        for next_value in iterator:
                            if next_value <= current_value:
                                list_line.remove(next_value)
                                break
                            current_value = next_value

                        problem_dampened = True
            if list_line[0] > list_line[1]:
                if not all(a > b for a, b in pairwise(list_line)): #Does everything Decrease?
                    if problem_dampened and not failed_line:
                        print(f"Two failures detected {list_line}")
                        failed_line = True
                    else:
                        iterator = iter(list_line)
                        current_value = next(iterator)
                        for next_value in iterator:
                            if next_value >= current_value:
                                list_line.remove(next_value)
                                break
                            current_value = next_value

                        problem_dampened = True
            if validate_difference_in_measurement(list_line):
                if problem_dampened and not failed_line:
                    print(f"Two failures detected {list_line}")
                    failed_line = True
                else:
                    iterator = iter(list_line)
                    current_value = next(iterator)
                    for next_value in iterator:
                        difference = abs(current_value - next_value)
                        if 1 < difference > 3:
                            list_line.remove(next_value)
                            break
                        current_value = next_value

                    problem_dampened = True
                    continue

        if i == 1:
            if not failed_line:
                valid_lines.append(list_line)
                dampened_valid_lines.append(list_line)

print(valid_lines)

# 566 569

    # Duplicate + Duplicate
    # Duplicate + Outside of

    # for value in list_line:
