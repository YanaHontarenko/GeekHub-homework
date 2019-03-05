# Write regular expression to ZIP codes UK.
import re
input_string = "yana.ho_ntar5645enko@gmail.rujjEC1Y 8SY 12.12.1998cewc c ewj23/34/1887ckw 23/4//21#!@#"

'''
Postcode: EC1Y 8SY
EC - postal area
1Y - postal district
8 - postal sector
SY - delivery point
For this regular expression think that delivery point is just two uppercase letter.
'''
# Read from file regular expression.
with open("readable_regex") as file:
    pattern = [row.strip() for row in file]
pattern_end = ' ' + pattern[-1]
print(pattern_end)
del pattern[-1]
check = [re.search(re.compile(pat), input_string) for pat in pattern]
if any(check):
    for item in check:
        if item:
            index = check.index(item)
    pattern_end = pattern[index] + pattern_end
    print(re.search(pattern_end, input_string).group())
