def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number ==  3:   
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:   
        result = 'Sunday'
    else:
        result = f'there arent {day_number} day in a week idiot'
        return result

day_number = int(input(f'input day number:'))
name = day_name(day_number)
print(f'the name of day {day_number} is {name}')