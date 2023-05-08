def add_time(start_time, time_to_add, day=None):
#   start time
    new_time = ""
    AMPM = start_time.split()
    start_time_split = AMPM[0]
    AMPM = AMPM[1]
    start_hours_minutes = start_time_split.split(":")
    start_hours = start_hours_minutes[0]
    start_minutes = start_hours_minutes[1]
    if AMPM == 'PM':
        PM_OFF_SET = 60 * 12
    elif AMPM == 'AM':
        PM_OFF_SET = 0
    else:
        return 'Start times need to have an "AM" or a "PM"'
    start_time_total = (int(start_hours) * 60) + int(start_minutes) + PM_OFF_SET
#   add time
    add_hours_minutes = time_to_add.split(":")
    add_hours = add_hours_minutes[0]
    add_min = add_hours_minutes[1]
    time_to_add_total = (int(add_hours) * 60) + int(add_min)
#   Total time
    total_time = start_time_total + time_to_add_total
#   answer
    total_hours = total_time//60
    end_minutes = total_time % 60
    total_days = 0
    while total_hours >= 24:
        total_hours = total_hours - 24
        total_days += 1

    if total_hours > 12:
        end_hours = total_hours - 12
        end_AMPM = 'PM'
    elif total_hours == 12:
        end_hours = 12
        end_AMPM = 'PM'
    elif total_hours == 0:
        end_hours = 12
        end_AMPM = 'AM'
    elif total_hours < 12:
        end_hours = total_hours
        end_AMPM = 'AM'

    new_time += ("{}:{:02d} {}".format(end_hours, end_minutes, end_AMPM))

    if day is not None:
        day = day.lower()
        days_of_week = {
            "1": "monday",
            "2": "tuesday",
            "3": "wednesday",
            "4": "thursday",
            "5": "friday",
            "6": "saturday",
            "7": "sunday"
        }

        days_of_week_upper = {
            "1": "Monday",
            "2": "Tuesday",
            "3": "Wednesday",
            "4": "Thursday",
            "5": "Friday",
            "6": "Saturday",
            "7": "Sunday"
        }

        days_of_week_swap = {v: k for k, v in days_of_week.items()}
        day_start_number = days_of_week_swap.get(day)
        end_day = int(day_start_number) + int(total_days)
        end_day = days_of_week_upper.get(str(end_day))
        new_time += (", {}".format(end_day))

    if total_days == 1:
        new_time += (" (next day)")
    elif total_days > 1:
        new_time += (" ({} days later)".format(total_days))
    return new_time


add_time("3:00 PM", "3:10", "wednesday")
