# Write a program to convert from Arabic numbers to Roman.
# Input: integer from 1 to 3999.
# Output: string.


def from_arabic_to_roman(number):
    arabic_roman =[
    [1, "I"], [4, "IV"], [5,"V"], [9, "IX"], [10, "X"], [40, "XL"], [50, "L"],
    [90, "XC"], [100, "C"], [400, "CD"], [500, "D"], [900, "CM"], [1000, "M"]
    ]
    result_string = ''
    biggest = len(arabic_roman) - 1
    while number > 0:
        while arabic_roman[biggest][0] > number:
            biggest = biggest - 1
        result_string = result_string + arabic_roman[biggest][1] * (number // arabic_roman[biggest][0])
        number = number % arabic_roman[biggest][0]
    return result_string


print(from_arabic_to_roman(2223))
