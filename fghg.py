day_in_week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

day_number = int(input("Enter day number (1-7): "))

if 1 <= day_number <= 7:
    print(day_in_week[day_number])
else:
    print("Incorrect day number. Please enter a number between 1 and 7.")