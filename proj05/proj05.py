# Name:
# Date:

# proj05: functions and lists
#list[0] = var to add something to the area?


def divisors(num):
    list = []
    list2 = []
    list3 = []

    numberr=0
    number = 1
    while number < num + 1:

        if num%number == 0:

            numberr=num/number

            list3.append(numberr)
        number = number + 1

    print list3[::-1]

    return list3[::-1]


divisors(15)

def prime(num):
    var = divisors(num)

    listc=[]
    numberr = 0


    if len(var) > 2:
        print "no not a prime"
        return False
    else:
        print "yes its a prime"
        return True


prime(8)

#PART TWOOOOOOOOO


def intersection(lst1, lst2):
    listt = []
    listtt = []
    if len(lst1) > len(lst2):
        biggerlst = lst1
        smallerlst = lst2
    else:
        biggerlst = lst2
        smallerlst = lst1
    for letter in smallerlst:
        if letter in biggerlst:
            listt.append(letter)
    return listt

#PART THREEEEEEE
#a ^2 + b^2 = c^2
def find_ab(side1, side2, side3):
    if side1 > side2 and side1 > side3:
        b=side2
        a=side3
        print"side 2 and side 3 are a and b"
    elif side2>side1 and side2>side3:

        b=side3
        a=side1
        print"side 1 and side 3 are a and b"
    else:

        b=side1
        a=side2
        "side 1 and side 2 are a and b"
    sides = [a,b]
    return a, b

def find_c(side1, side2, side3):
    if side1 > side2 and side1 > side3:
        c = side1
        print "side 1 is the hypotenuse"
    elif side2 > side1 and side2 > side3:
        c = side2
        print "side 2 is the hypotenuse"
    else:
        c= side3
        print"side 3 is the hypotenuse"
    hypotenuse = [c]
    return c
def square(side):
    side = side * side
    print "that number squared is", side
    return side
def pythagorean(a, b, c):
    a = side1
    b = side2
    c = side3
    if side1 > side2 and side1 > side3:
        a = side2
        b = side3
        c = side1
    elif side2 > side1 and side2 > side3:
        c = side2
        b = side3
        a = side1
    else:
        c = side3
        b = side2
        a = side1
    a2 = a * a
    b2 = b * b
    c2 = c * c
    if a2 +b2 == c2:
        return True




















# Part II

#def intersection(lst1, lst2):
    #"""
    #Takes two lists and returns a list of the elements in common between the lists
    #:param lst1: list, any type
    #:param lst2: list, any type
    #:return: list, any type
    #"""
    #return ["test"]

# Part III

def find_ab(side1, side2, side3):
    """
    Takes three side lengths an returns two smallest in a list
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: list of 2 ints or floats
    """
    return [0, 0]

def find_c(side1, side2, side3):
    """
    Takes three side lengths an returns the largest
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: int or float
    """
    return 0

def square(side):
    """
    Takes a side length and returns the side length squared
    :param side: int or float
    :return: int or float
    """
    return 0

def pythagorean(a,b,c):
    """
    Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :return: bool
    """
    return False

def is_right(side1, side2, side3):
    """
    Takes three side lengths and returns true if triangle is right
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: bool
    """
    return False

# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")
