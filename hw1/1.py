# Input: string with punctuation marks.
# Words are separated by a space.
# After punctuation marks, the space always stands.
# Output: a list of unique words into which the string can be divided,
# without punctuation marks.
# Remove brackets and quotes that are adjacent to the word in front or behind
import re

input_string = str("\"Все йде, все минає і краю немає , \n Куди ж воно ділось? відкіля взялось! \n І дурень, і мудрий нічого не знає. \n Живе... умирає... одно зацвіло , \n А друге зав’яло, навіки зав’яло... \n І листя пожовкле вітри рознесли.\"")
input_string = re.sub('[.,?! \n]+', ' ', input_string)
input_string = re.sub('(^\W+)|(\W+$)', '', input_string)
input_string = input_string.lower()
list_result = list(set(input_string.split(' ')))
print(list_result)