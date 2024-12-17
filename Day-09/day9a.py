from itertools import product

import numpy as np

def open_file(file_name):
    with open(f'./{file_name}', 'r') as file:
        the_file = file.readline()
        #the_file = file.readlines()
        the_file = list(the_file.strip())
        #file_grid = np.array(the_file)
    return the_file

def generate_file_details(disk_to_defrag):
    parsed_files = [
        (disk_to_defrag[i], disk_to_defrag[i + 1]
        if i + 1 < len(disk_to_defrag) else '0')
        for i in range(0, len(disk_to_defrag), 2)
    ]

    file_contents = []
    file_id = 0
    for parsed_file in parsed_files:
        for i in range(int(parsed_file[0])):
            file_contents.append(file_id)
        for i in range(int(parsed_file[1])):
            file_contents.append('.')
        file_id += 1

    return file_contents, parsed_files

def defrag_parsed_file(file_combinations: list):
    for i in range(len(file_combinations) - 1, 0, -1):
        open_id = file_combinations.index(".")
        if open_id < i:
            file_combinations[open_id] = file_combinations[i]
            file_combinations[i] = "."
        else:
            break # Disk has been defragged

    return file_combinations

def defrag_but_retain_coherency(file_combinations: list, parsed_files: list[tuple[str, str]]):
    for file_id in range(len(parsed_files) - 1, 0, -1):
        print(file_id)
        file_length = int(parsed_files[file_id][0])
        file_position = file_combinations.index(file_id)

        for index, new_value in enumerate(file_combinations):
            if new_value == ".":
                if check_that_we_have_space(index, file_combinations, file_length):
                    if file_position > index:
                        for i in range(len(file_combinations)):
                            if file_combinations[i] == file_id:
                                file_combinations[i] = "."

                        for i in range(file_length):
                            file_combinations[index + i] = file_id
                        break

    return file_combinations


def check_that_we_have_space(index, file_combinations, file_length):
    open_space = 0
    for file_part in range(file_length):
        if index + file_part >= len(file_combinations):
            return False
        if file_combinations[index + file_part] == ".":
            open_space += 1

    if open_space == file_length:
        return True
    return False


def calculate_checksum(defragged_file):
    checksum_value = 0
    for i in range(len(defragged_file)):
        defragged_value = defragged_file[i]
        if defragged_value == ".":
            defragged_value = 0
        checksum_value += int(defragged_value) * i
    return checksum_value

if __name__ == '__main__':
    disk_to_defrag = open_file(file_name='input-1.txt')
    file_combinations, parsed_files = generate_file_details(disk_to_defrag)

    defragged_file = defrag_parsed_file(file_combinations)
    defragged_file_checksum = calculate_checksum(defragged_file)
    defragged_coherent_file = defrag_but_retain_coherency(file_combinations, parsed_files)
    defragged_coherent_file_checksum = calculate_checksum(defragged_coherent_file)

    print(defragged_file_checksum)
    print(defragged_coherent_file_checksum)

    var = True