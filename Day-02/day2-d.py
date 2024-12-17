def do_all_differences_increase(differences: [int]):
    for difference in differences:
        if difference > 0:
            if difference < 4:
                var = True
            else:
                return False
        else:
            return False
    return True


def do_all_differences_decrease(differences: [int]):
    for difference in differences:
        if difference < 0:
            if difference > -4:
                var = True
            else:
                return False
        else:
            return False
    return True

def can_we_dampen_problem(list_line: [int]):
    '''Yes we can'''
    #Loop through each value in list_line, remove that value then test, if we fail, use the next value
    #If by the final value we still fail, return False
    for i in range(0, len(list_line)):
        test_line = list_line.copy()
        test_line.pop(i)

        iterator = iter(test_line)
        current_value = next(iterator)
        all_differences = []
        for next_value in iterator:
            difference = next_value - current_value
            all_differences.append(difference)
            current_value = next_value

        var = True
        if do_all_differences_increase(all_differences) or do_all_differences_decrease(all_differences):
            return True
    return False


list_lines = []
with open('./input-1.txt', 'r') as file:
    read_lines = file.readlines()

for line in read_lines:
    line = line.replace('\n', '')
    string_list = line.split(' ')
    list_lines.append(list(map(int, string_list)))

valid_lines = []
for list_line in list_lines:
    iterator = iter(list_line)
    current_value = next(iterator)
    all_differences = []
    for next_value in iterator:
        difference = next_value - current_value
        all_differences.append(difference)
        current_value = next_value

    if do_all_differences_increase(all_differences) or do_all_differences_decrease(all_differences):
        valid_lines.append(list_line)
    else:
        if can_we_dampen_problem(list_line):
            valid_lines.append(list_line)


print(valid_lines)