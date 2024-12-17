import re

with open('./input-1.txt', 'r') as file:
    # Part 2:
    enabled_lines = re.findall(r"(do\(\))(.*?)(don't\(\))", file.read())
    enabled_line = "".join(line[1] for line in enabled_lines)
    parsed_mults = re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\))', enabled_line)

    # Part 1:
    # parsed_mults = re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\))', file.read())

total_value = 0
for mult in parsed_mults:
    mult_values = mult.replace('mul(', '').replace(')', '').split(',')
    mult_value = int(mult_values[0]) * int(mult_values[1])
    total_value += mult_value

print(parsed_mults)
print(total_value)