# Write regular expression.
import re

input_string = "yana.ho_ntar5645enko@gmail.rujjb33/02/1905cw we212:18:59+380978134523inc 12.12.1998cewc c ewj23/34/1887ckw 23/4//21#!@#"

# Time in format HH:MM:SS.

pattern_1 = r'([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
print(re.search(pattern_1, input_string).group())

# Phone number in format +38xx-xxx-xx-xx.

pattern_2 = r'(\+380(50|6[3678]|9[3|5-9])\d{7})'
print(re.search(pattern_2, input_string).group())

# Date in format DD.MM.YYYY or DD/MM/YYYY.

pattern_3 = r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])[\.\/](0[1-9]|1[0-2])[\.\/]\d{4}'
print(re.search(pattern_3, input_string).group())

# E-mail adress.

pattern_4 = r'([a-zA-Z0-9\.-_]+@[a-zA-Z]+\.(com|ru|ua))'
print(re.search(pattern_4, input_string).group())
