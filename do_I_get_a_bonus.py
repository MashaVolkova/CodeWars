def bonus_time(salary, bonus):
    if bonus == True:
        result1 = salary * 10
    else:
        result1 = salary
    return result1

result = '${}'.format(bonus_time(salary, bonus))
print(result)
