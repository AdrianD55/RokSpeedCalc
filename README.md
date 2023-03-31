# RokSpeedCalcV2.0

The code is a Python script that calculates the total amount of speedups a user has based on the input they provide for various time durations. It makes use of a dictionary called time_durations which contains the names of different time durations as keys and the number of minutes they represent as values. The script prompts the user to enter the number of speedups they have for each time duration and calculates the total amount of speedups in minutes.

The function handle_input(duration_name, duration_minutes) takes two arguments: duration_name, which is a string representing the name of the time duration, and duration_minutes, which is an integer representing the number of minutes in that time duration. The function repeatedly prompts the user to input the number of speedups they have for the given time duration until a valid integer is entered. It then calculates the total number of minutes the speedups represent and returns this value.

The main part of the script creates a variable total_minutes initialized to 0 and iterates over each key-value pair in time_durations. For each time duration, it calls the handle_input() function with the name and number of minutes for that duration and adds the returned value to total_minutes.

After all the time durations have been processed, the script calculates the total number of days, hours, and minutes the speedups represent. It divides the total number of minutes by 1440 to get the total number of days, takes the remainder of this division to get the leftover minutes, divides the leftover minutes by 60 to get the number of hours, and takes the remainder of this division to get the remaining minutes.

Finally, the script prints out the total amount of speedups in days, hours, and minutes using the print() function. The output is a string that includes the total number of days, hours, and minutes separated by spaces and labeled accordingly. 
