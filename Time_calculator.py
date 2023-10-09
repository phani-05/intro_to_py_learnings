def add_time(start, duration, starting_day=None):
    # Define a dictionary to map days of the week to their indices
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split the input start time into hours, minutes, and AM/PM
    start_parts = start.split()
    start_time = start_parts[0].split(":")
    start_hour = int(start_time[0])
    start_minute = int(start_time[1])
    am_pm = start_parts[1]

    # Split the input duration time into hours and minutes
    duration_parts = duration.split(":")
    duration_hour = int(duration_parts[0])
    duration_minute = int(duration_parts[1])

    # Calculate the total minutes
    total_minutes = (start_hour * 60 + start_minute + duration_hour * 60 + duration_minute)

    # Calculate the new time and days later
    new_hour = total_minutes // 60 % 12
    if new_hour == 0:
        new_hour = 12  # 12:00 AM instead of 0:00 AM
    new_minute = total_minutes % 60
    new_am_pm = "AM" if total_minutes // 60 < 12 else "PM"

    # Calculate days later
    days_later = total_minutes // (24 * 60)

    # Calculate the new day of the week
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        if days_later == 1:
            new_day = f", {new_day}"
        elif days_later > 1:
            new_day = f", {new_day} ({days_later} days later)"
        else:
            new_day = ""

    # Construct the result string
    if starting_day:
        result = f"{new_hour}:{str(new_minute).zfill(2)} {new_am_pm}{new_day}"
    else:
        result = f"{new_hour}:{str(new_minute).zfill(2)} {new_am_pm}"
    
    return result
