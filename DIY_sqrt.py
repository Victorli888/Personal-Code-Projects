# Question: Find the square root on an integer without using a Library

def square(target, i, j):
    """
    Using our Binary Search Algorithm find a sqrt of a target or with within .001 accuracy

    :param target: the value we need to find the sqrt for
    :param i: Lower number (maximum)
    :param j: upper number (minimum)
    :return: the Square Root of our Target
    """
    mid = (i + j) / 2
    mult = mid * mid  # we are searching a value from our lower and upper range that will match our target

    if mult == target or (abs(mult-target)) < .001:
        return mid
    elif mult < target:
        return square(target, mid, j)
    else:
        return square(target, i, mid)

def findSqrt(target):
    """
    Start at 1 and multiply itself for a square, if it hits our target then we've found our sqrt
    else we will keep searching for it
    :param target: the value we need to find the sqrt for
    :return: The Square root of our target
    """
    i = 1  # Our starting number
    searching = True

    while searching:  # keep searching until false
        mult = i*i  # if squaring our initial == our target we've found our sqrt

        if mult == target:
            print(i)
            searching = False
        elif mult > target:
            result = square(target, i-1, i)
            print("{0:.3f}".format(result))
            searching = False
        i += 1


if __name__ == '__main__':
    target = int(input("Enter number to find square root: "))
    findSqrt(target)


"""
1. Starting at i = 1 we want to square our numbers to find if they equal our target
2. increment it by i = 1 such that, 1*1, 2*2, 3*3 until either we hit our target or i is > than target
3. When its larger we know that its' sqrt is somewhere in that square between our increments
4. Search for the sqrt with Binary Search, with n - target; i - lower number j - upper number
5. Find the mid pt of our i & j and square it then make the following comparisons:
    a. did we find our target?
    b. is our (midpt)^2 bigger than our target?, lower our upper number to the mid pt (Recurse)
    c. is our (midpt)^2 smaller than our target?, increase our lower number to the mid pt (Recurse)
"""