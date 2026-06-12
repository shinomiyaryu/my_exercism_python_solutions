def equilateral(sides):
    if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
        if sides[0] == sides[1] and sides[0] == sides[2]:
            if sides[0] != 0:
                return True
    return False
    #pass


def isosceles(sides):
    if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
        if sides[0] == sides[1]:
            return True
        if sides[0] == sides[2]:
            return True
        if sides[1] == sides[2]:
            return True
    return False
    #pass


def scalene(sides):
    if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
    return False
    #pass
