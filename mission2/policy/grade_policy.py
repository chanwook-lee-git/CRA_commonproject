def get_grade(point):
    if point >= 50:
        return "GOLD"
    elif point >= 30:
        return "SILVER"
    else:
        return "NORMAL"