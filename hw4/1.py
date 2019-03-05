import numpy as np
# Demonstration of work with library numpy.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print([iris[:3]])

# Remove the column 'species'.
iris = np.delete(iris, names.index('species'), 1)
print(iris[:3])

# Convert the first 4 columns to a 2D array.
iris = np.array(iris, dtype='float')
print(iris[:3])

# Calculate mean, median, standart deviation on 1 column.
print(np.mean(iris[:, 0]))
print(np.median(iris[:, 0]))
print(np.std(iris[:, 0]))

# Insert 20 values np.nan on random place in array.
np.put(iris, np.random.choice(range(iris.shape[0] * iris.shape[1]), 20, replace=False), np.nan)
print(iris)

# Find the position of the inserted values np.nan in the 1st column.
print(np.where(np.isnan(iris[:, 0])))

'''
Filter an array by the condition of the value
in the 3rd column> 1.5 And the values in the 1st column <5.0.
'''
modificated = iris[np.logical_and(iris[:, 2] > 1.5, iris[:, 0] < 5)]
print(modificated)

# Replace all np.nan values with 0.
indixes = np.isnan(iris)
iris[indixes] = 0
print(iris)

# Count all unique values in the array and print them together with their counted number.
uniqs, counts = np.unique(iris, return_counts=True)
print("Unique items : ", uniqs)
print("Their counts : ", counts)

# Split array on two arrays horizontally.
array_one, array_two = np.vsplit(iris, 2)
print(iris.shape, array_one.shape, array_two.shape)

# Sort both arrays by the 1st column: 1st ascending, 2nd descending.
print(array_one)
print(array_two)
array_one = array_one[np.argsort(array_one[:, 0])]
array_two = array_two[np.argsort(array_two[:, 0])]
print(array_one)
print(array_two)

# Concatenate both arrays.
iris = np.concatenate([array_one, array_two], axis=0)
print(iris)

# Find the most repeated value in the array.
uniqs, counts = np.unique(iris, return_counts=True)
print(uniqs[np.argmax(counts)])

'''
Write function, which multiply all values in column < mean value on 2
and divide all other values on 4. Apply to the 3rd column.
'''


def transform_column(x):
    mean_values = np.mean(x)
    print(mean_values)
    return [value * 2 if value > mean_values else value / 4 for value in x]


iris[:, 2] = transform_column(iris[:, 2])
print(iris)
