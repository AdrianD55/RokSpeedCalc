def handle_input(duration_name, duration_minutes):
    while True:
        speedups = input(f"How many {duration_name} speedups do you have? ")
        try:
            speedups = int(speedups)
            speedups_minutes = speedups * duration_minutes
            return speedups_minutes
        except ValueError:
            print("Error! Please enter a number.")


time_durations = {
    "1 minute": 1,
    "5 minutes": 5,
    "10 minutes": 10,
    "15 minutes": 15,
    "30 minutes": 30,
    "60 minutes": 60,
    "3 hours": 180,
    "8 hours": 480,
    "15 hours": 900,
    "24 hours": 1440,
    "3 days": 4320,
    "7 days": 10080,
}

total_minutes = 0
for duration_name, duration_minutes in time_durations.items():
    total_minutes += handle_input(duration_name, duration_minutes)

total_days = total_minutes // 1440
leftover_minutes = total_minutes % 1440
hours = leftover_minutes // 60
remaining_minutes = leftover_minutes % 60

print(
    "Your total speedups are:",
    str(total_days),
    "Days",
    str(hours),
    "Hours",
    str(remaining_minutes),
    "Minutes",
)
