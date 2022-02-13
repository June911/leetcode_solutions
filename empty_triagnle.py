# find the area of a triangle with coordinates
# https://math.stackexchange.com/questions/516219/finding-out-the-area-of-a-triangle-if-the-coordinates-of-the-three-vertices-are/516223
from itertools import combinations

"""
find all empty triangles in the X, Y 
1. equal area sum 
2. not in the line 
"""

def area_tri(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    # Calculate area of triangle ABC
    A = area_tri(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    A1 = area_tri(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    A2 = area_tri(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    A3 = area_tri(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


# check if x,y does not lie on the line of (x1, y1), (x2, y2), (x3, y3)
def isnotOnline_all(x1, y1, x2, y2, x3, y3, x, y):
    isOnline_any = isOnline(x1, y1, x2, y2, x, y) | isOnline(x1, y1, x3, y3, x, y) \
                   | isOnline(x2, y2, x3, y3, x, y) | isOnline(x1, y1, x2, y2, x3, y3, Check_inside=False)

    return (not isOnline_any)


# check if x,y lies on the line of (x1, y1), (x2, y2)
def isOnline(x1, y1, x2, y2, x, y, Check_inside = True):
    if x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)
    else:
        slope = ""

    if x - x1 != 0:
        slope2 = (y - y1) / (x - x1)
    else:
        slope2 = ""

    # if it is ok that the point x is on the extension of the line
    if Check_inside:

        con_x = max(abs(x- x1), abs(x - x2)) < abs(x1 - x2)
        con_y = max(abs(y- y1), abs(y - y2)) < abs(y1 - y2)
        con = (slope2 == slope) & con_x & con_y
    else:
        con = slope2 == slope

    if con:
        return True
    else:
        return False


def solution(X, Y):
    # number of points
    n = len(X)
    # set of total points
    s = set(range(n))

    # all possible_solution of triangles

    possible_solution = list(combinations(list(range(0,n)), 3))

    for i in range(len(possible_solution)):
        # coordinates of the triangle
        coor_tri = possible_solution[i]

        # more specifically
        x1 = X[coor_tri[0]]
        y1 = Y[coor_tri[0]]

        x2 = X[coor_tri[1]]
        y2 = Y[coor_tri[1]]

        x3 = X[coor_tri[2]]
        y3 = Y[coor_tri[2]]

        other_points = list(s - set(coor_tri))
        con_empty_tri = True
        for j in other_points:
            # not isInside and not on the line ==> empty
            con_isInside = isInside(x1, y1, x2, y2, x3, y3, X[j], Y[j])
            con_notOnline = isnotOnline_all(x1, y1, x2, y2, x3, y3, X[j], Y[j])
            con_empty_tri = con_empty_tri & (not con_isInside) & con_notOnline
            # print(con_isInside, con_notOnline, con_empty_tri)

        if con_empty_tri:
            print(coor_tri)
            # return coor_tri


if __name__ == '__main__':

    X = [1, 4, 3, 2, 3]
    Y = [4, 3, 1, 1, 2]

    solution(X,Y)

    X = [0, 1, 2, 4, 4, 5, 6]
    Y = [0, 1, 2, 3, 4, 5, 6]
    solution(X,Y)
