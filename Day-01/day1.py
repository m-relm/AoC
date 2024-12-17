# Open the file and read lines
with open('./input-1.txt', 'r') as file:
    lines = file.readlines()

# Process each line
left_data = []
right_data = []
multiplier = []
data = []
for line in lines:
    values = line.strip().split('   ')
    left_data.append(values[0])
    right_data.append(values[1])
    multiplier.append(0)

for i in range(len(left_data)):
    for right_value in right_data:
        if left_data[i] == right_value:
            multiplier[i] += 1

output = 0
for i in range(len(left_data)):
    output += int(left_data[i]) * multiplier[i]


print(output)