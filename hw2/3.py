# The coordinates of three points are given, but they are written as a string:"(x1, y1), (x2, y2), (x3, y3)".
# x1, y1, x2, y2, x3, y3 are numbers.You need to find the circle passing through these points
# and return the equation of the circle.
# Remove extra zeros and periods if they are not needed. For rounding, use a standard mathematical rule.
# Input:string of coordinates.
# Output:string of circle quation.
import re
from math import sqrt


# Formating string.
# From string "(1, 2), (3, 2), (2, 3)" -> lists of integers [1, 3, 2]; [2, 2, 3]
def format_str(string):
    string = re.sub('[(), ]+', ' ', string)
    string = re.sub('(^\W+)|(\W+$)', '', string)
    string = string.split(" ")
    list_of_coordinates = list(map(int, string))
    return list_of_coordinates[0:5:2], list_of_coordinates[1:6:2]

def clear_float_if_possible(number):
    number = round(number, 2)
    if number % 1 < 0.001:
        number = int(number)
    return number

# Function in which we search center of circle and it`s radius
def find_x_y_r(x, y):
    # Calculate line slope factor
    m_a = (y[1] - y[0]) / (x[1] - x[0])
    m_b = (y[2] - y[1]) / (x[2] - x[1])
    # Circle dosn`t exist if line slope difference equal 0 (lines parallel)
    if m_b - m_a == 0:
        return 0, 0, 0
    x0 = ((m_a * m_b * (y[0] - y[2])) + (m_b * (x[0] + x[1])) - (m_a * (x[1] + x[2]))) / (2 * (m_b - m_a))
    # Or if line slope equal 0(in our case it means that the lie on same horizontally line)
    # If it is true I use line slope other line to equal y0
    if m_a == 0:
        y0 = -(1 / m_b) * (x0 - ((x[1] + x[2]) / 2)) + ((y[1] + y[2]) / 2)
    else:
        y0 = -(1 / m_a) * (x0 - ((x[0] + x[1]) / 2)) + ((y[0] + y[1]) / 2)
    r = sqrt((x[0] - x0)**2 + (y[0] - y0)**2)
    return clear_float_if_possible(x0), clear_float_if_possible(y0), clear_float_if_possible(r)


def circle_equation(string):
    x, y = format_str(string)
    # If two points lie on the same vertical line, change the order of the points so that there are no vertical lines
    # Otherwise order P1P2 P3P2, where P1 - first point
    if len(set(x)) != len(x):
        if x[0] == x[1]:
            x0, y0, r = find_x_y_r([x[0], x[2], x[1]], [y[0], y[2], y[1]])
        elif x[0] == x[2]:
            x0, y0, r = find_x_y_r([x[0], x[1], x[2]], [y[0], y[1], y[2]])
        else:
            x0, y0, r = find_x_y_r([x[2], x[0], x[1]], [y[2], y[0], y[1]])
    else:
        x0, y0, r = find_x_y_r([x[0], x[1], x[2]], [y[0], y[1], y[2]])
    if x0 == 0 and y0 == 0 and r == 0:
        return "Circle does not exist"
    # Make output string 
    if x0 < 0:
        result_string = "(x+" + str(x0 * -1)
    else:
        result_string = "(x-" + str(x0)
    if y0 < 0:
        result_string = result_string + ")^2+(y+" + str(y0 * -1) + ")^2=" + str(r) + "^2"
    else:
        result_string = result_string + ")^2+(y-" + str(y0) + ")^2=" + str(r) + "^2"
    return result_string


#print(circle_equation("\"(1, 8), (-2, -7), (-4, -17)\""))
#print(circle_equation("\"(0, 1), (2, 0), (3, -1)\""))
#print(circle_equation("\"(2, 2), (2, 4), (5, 5)\""))
#print(circle_equation("\"(2, 2), (4, 2), (2, 4)\""))
print(circle_equation("\"(7,3),(9,6),(3,6)\""))