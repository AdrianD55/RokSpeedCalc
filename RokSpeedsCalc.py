total_minutes = 0
while True:
    one_minute = input("How many 1 minute speedups do you have? ")
    try:
        one_minute = int(one_minute)
        one_speeds = (one_minute * 1)
        total_minutes += one_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    five_minute = input("How many 5 minute speedups do you have? ")
    try:
        five_minute = int(five_minute)
        five_speeds = (five_minute * 5)
        total_minutes += five_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    ten_minute = input("How many 10 minute speedups do you have? ")
    try:
        ten_minute = int(ten_minute)
        ten_speeds = (ten_minute * 10)
        total_minutes += ten_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    fifteen_minute = input("How many 15 minute speedups do you have? ")
    try:
        fifteen_minute = int(fifteen_minute)
        fifteen_speeds = (fifteen_minute * 15)
        total_minutes += fifteen_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    thirty_minute = input("How many 30 minute speedups do you have? ")
    try:
        thirty_minute = int(thirty_minute)
        thirty_speeds = (thirty_minute * 30)
        total_minutes += thirty_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    sixty_minute = input("How many 60 minute speedups do you have? ")
    try:
        sixty_minute = int(sixty_minute)
        sixty_speeds = (sixty_minute * 60)
        total_minutes += sixty_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    three_hour = input("How many 3 hour speedups do you have? ")
    try:
        three_hour = int(three_hour)
        three_h_speeds = (three_hour * 180)
        total_minutes += three_h_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    eight_hour = input("How many 8 hour speedups do you have? ")
    try:
        eight_hour = int(eight_hour)
        eight_h_speeds = (eight_hour * 480)
        total_minutes += eight_h_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    fifteen_hour = input("How many 15 hour speedups do you have? ")
    try:
        fifteen_hour = int(fifteen_hour)
        fifteen_h_speeds = (fifteen_hour * 900)
        total_minutes += fifteen_h_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    twenty_four_hour = input("How many 24 hour speedups do you have? ")
    try:
        twenty_four_hour = int(twenty_four_hour)
        twenty_four_h_speeds = (twenty_four_hour * 1440)
        total_minutes += twenty_four_h_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    three_day = input("How many 3 day speedups do you have? ")
    try:
        three_day = int(three_day)
        three_day_speeds = (three_day * 4320)
        total_minutes += three_day_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

while True:
    seven_day = input("How many 7 day speedups do you have? ")
    try:
        seven_day = int(seven_day)
        seven_day_speeds = (seven_day * 10080)
        total_minutes += seven_day_speeds
        break
    except ValueError:
        print("Error! Please enter a number.")

total_days = total_minutes // 1440
leftover_minutes = total_minutes % 1440
hours = leftover_minutes // 60
remaining_minutes = leftover_minutes % 60

print("Your total speedups are:", str(total_days), "Days", str(hours), "Hours", str(remaining_minutes), "Minutes")
