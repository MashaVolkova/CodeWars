def century(year):
    if year % 100 == 0:
        century = year // 100
    if year in range(0, 100):
        century = 1
    if year % 100 != 0:
        century = (year // 100) + 1

    return century
