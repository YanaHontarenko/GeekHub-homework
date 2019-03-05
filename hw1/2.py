# Given a random list consisting of 0 and 1.
# Find the index at which begins the longest continuous sequence 1.
# If there are several such, it is enough to indicate the index of the first one.
random_list = [
    1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1
]

random = ''.join(list(map(str, random_list)))
max_sequence = max(random.split('0'))
print(random.index(max_sequence))