def score(x, y):
    magnitude = (x**2 + y**2)**(0.5)
    if 5 < magnitude <= 10:
        return 1
    if 1 < magnitude <= 5:
        return 5
    if magnitude <= 1:
        return 10
    return 0
    #pass
