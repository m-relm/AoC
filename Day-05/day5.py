with open('./input-1.txt', 'r') as file:
    safety_manuals = file.readlines()
    parsed_manuals = []
    for safety_manual in safety_manuals:
        safety_manual = safety_manual.strip().split(',')
        parsed_manuals.append(safety_manual)

with open('./input-2.txt', 'r') as file:
    page_rules = file.readlines()
    parsed_rules = []
    for page_rule in page_rules:
        parsed_rule = page_rule.strip().split('|')
        parsed_rules.append(parsed_rule)

valid_manuals = []
invalid_manuals = []
middle_values = []
for manual in parsed_manuals:
    valid_manual = True
    for rule in parsed_rules:
        page_before = rule[0]
        page_after = rule[1]

        if page_before in manual:
            if page_after in manual:
                before_order = manual.index(page_before)
                after_order = manual.index(page_after)
                if before_order > after_order:
                    valid_manual = False

    if valid_manual:
        middle_page = len(manual) // 2
        middle_value = manual[middle_page]

        valid_manuals.append(manual)
        middle_values.append(int(middle_value))
    else:
        invalid_manuals.append(manual)
valid_middle_sum = sum(middle_values)

corrected_manuals = []
corrected_middles = []
for manual in invalid_manuals:
    re_run = True
    while re_run:
        re_run = False
        for rule in parsed_rules:
            page_before = rule[0]
            page_after = rule[1]

            if page_before in manual:
                if page_after in manual:
                    before_order = manual.index(page_before)
                    after_order = manual.index(page_after)
                    if before_order > after_order:
                        manual.remove(page_after)
                        manual.insert(before_order, page_after)
                        re_run = True

    middle_page = len(manual) // 2
    middle_value = manual[middle_page]

    corrected_manuals.append(manual)
    corrected_middles.append(int(middle_value))

corrected_middle_sum = sum(corrected_middles)

var = True
print(parsed_rules)
