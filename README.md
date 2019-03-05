My homeworks for GeekHub Data Science course.
=============================================
**Homework №1**

*Task 1*

Given a string containing text with punctuation. Words are separated by a space. The space always stands after punctuation marks. Task: break the line into unique words without punctuation marks ("All" = "all"). Remove brackets and quotes that are adjacent to the word in front or behind.

*Task 2*

Given a random list, consisting of 0 and 1. Find the index from which the longest continuous sequence of 1 begins. If there are several such, it is enough to indicate the index of the first one.

*Task 3*

You have a histogram. Try to find the size of the largest rectangle that can be constructed from it`s columns. Examples of input -> output:
- [5] -> 5;
- [5, 3] -> 6;
- [1, 1, 4, 1] -> 4;
- [1, 1, 3, 1] -> 4;
- [2, 1, 4, 5, 1, 3, 3] -> 8.

**Homework №2**

*Task 1*

Write a program to convert from Arabic numbers to Roman. Input: an integer from 1 to 3999. The output is a string.

*Task 2*

Given the number N. Find the smallest positive integer X, such that the product of its digits will be equal to N. If X does not exist, return 0. Example: N = 20. We can decompose this number as 2 * 10, but 10 is not a number. You can also decompose N as 4 * 5 or 2 * 2 * 5. The smallest number for 2 * 2 * 5 is 225, for 4 * 5 -45. Result 45.
Input: the number N, as an integer (int). The source number ranges from 9 to 10,000. Output: the number X, as an integer (int).

*Task 3*

Through any three points that do not lie on one line, you can draw only one circle. Given the coordinates of three points, but they are written as a string: "(x1, y1), (x2, y2), (x3, y3)". Where x1, y1, x2, y2, x3, y3 are numbers. You need to find the circle passing through these points and return the equation of the circle. In a Cartesian coordinate system (with X and Y axes), a circle centered on (x0, y0) coordinates and radius r will be described by the following equation: "(x-x0) ^ 2 + (y-y0) ^ 2 = r ^ 2 ". Where x0, y0, r are decimal numbers rounded to two decimal places. Remove extra zeros and periods if they are not needed. For rounding, use a standard mathematical rule. Input: Coordinates as string (str, unicode). Output: Equation of a circle, as a string (str, unicode).

**Homework №3**

Using classes, describe any process or system known to you:
- at least once it is necessary to use inheritance, private method and (or) private attribute; 
- each module, class, public method and function (if you use) should have a short description in English (docstring); 
- public methods and __init __ () need, if possible, to specify the type of incoming and return data; 
- use static and class method, property;
- use the magic method.

**Homework №4**

1. Import dataset Iris.
>url = 'ttps://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

>iris = np.genfromtxt(url, delimhiter=',', dtype='object')
2. Remove the column 'species'.
3. Convert the first 4 columns to a 2D array.
4. Calculate mean, median, standard deviation on the 1st column.
5. Insert 20 values of np.nan to random positions in the array.
6. Find the position of the inserted values np.nan in the 1st column.
7. Filter an array by the condition of the value in the 3rd column is greater than 1.5 and the values in the 1st column are less than 5.0.
8. Replace all np.nan values with 0.
9. Count all unique values in the array and list them together with the counted number..
10. Split an array horizontally into 2 arrays.
11. Sort both resulting arrays by the 1st column: 1st ascending, 2nd descending.
12. Merge both arrays.
13. Find the most repeated value in the array.
14. Write a function that would multiply all the values in the column, less than the average value in this column, by 2, and divide the remaining values by 4. Apply to the 3rd column.

**Homework №5**

Write regular expression for: 
- Time in format HH:ММ:SS.
- Mobile phone in format +38xx-xxx-xx-xx. 
- Data in format DD.ММ.YYYY or DD/ММ/YYYY. 
- Email.
- ZIP codes UK.

[File readable_regex](hw5/readeble_regex) contain regular expression for zip codes of UK split by "|". It was create because full regular expression don`t readable from file. [Full regular expression](hw5/regex).

**Homework №6**

Some tasks for practice in using dataFrames with Pandas.

**Homework №7**

Some tasks for practice in visualization using matplotlib, seaborn.

**Homework №8**

First three weeks from the final project of specialization MPTI and Yandex ["Machine learning and data analysis"](https://datasciencecourse.ru/). 
(*Week 2 isn`t full*)

**Homework №9**

*Task 1*

Full second week from ["Machine learning and data analysis"](https://datasciencecourse.ru/).

*Task 2*

1. Make a 2 dice throw simulator(20,000 rolls). 
2. Check the probability of falling each numbers on each dice.
3. Build a histogram of the fallinf sums of numbers on the dices.
4. Make 10,000 series of rolls. In each series determines the number of rolls before the amount on the dice was 9. 
5. Visualizate the result.
6. Generate a sequence of random numbers in the range from 0 to 12, with a normal distribution.
7. Visualizate the result.
8. Generate 2 random sequences. Get a third sequence, each element of which is the sum of the corresponding elements of the first two sequences.
9. Visualizate the result.
10. Check that the distribution obtained corresponds to the normal distribution.
11. From the two previous sequences, get a fourth sequaence, each element of which is equal to the ratio of the corresponding elements from the first sequence to the element of the second sequence.
12. Visualizate the result.
13. Check whether the resulting sequence complies with the normal distribution.
14. Generate two new random sequences with different RandomState.
15. Visualizate the result.
16. Check the correlation of these two sequences.

**Homework №10**

Use the learned model to solve the regression or classification problem on [data](https://archive.ics.uci.edu/ml/datasets/wine+quality). (It means that this problem can be solved in two ways).

**Homework №11**

Fourth week from ["Machine learning and data analysis"](https://datasciencecourse.ru/).
