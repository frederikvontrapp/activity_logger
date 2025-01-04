# modules
import time
import csv
import mouse
import keyboard


# functies
def log_activity():
    global activity_detected, last_activity
    activity_detected = True
    last_activity = time.time()

def calculate_time_parts(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds


# variabelen
log_file = '/home/saartje/exe/programmeren/python/pc_tijd_loggen/pc_tijd_loggen.csv'
activity_detected = False
last_activity = time.time()
date_today = time.strftime("%Y_%m_%d")


# start luisteren
keyboard.on_press(lambda _:log_activity())

# hoofd loop
while not activity_detected:
    time.sleep(0.1)

while activity_detected:
    current_time = time.time()
    time_passed = current_time - last_activity

    print(f"Time passed: {time_passed:.0f} seconds")

    time.sleep(1)

    if time_passed >= 5:

        with open(log_file, "r") as file:
            rows = list(csv.reader(file))

        for i, row in enumerate(rows):
            if len(row) < 4:
                continue

            if date_today in row[0]:
                new_hours, new_minutes, new_seconds = calculate_time_parts(round(time_passed))
                old_hours, old_minutes, old_seconds = map(int, row[1:4])

                new_hours_total = new_hours + old_hours + (new_minutes + old_minutes) // 60
                new_minutes_total = (new_minutes + old_minutes) % 60 + (new_seconds + old_seconds) // 60
                new_seconds_total = (new_seconds + old_seconds) % 60

                rows[i] = [date_today, new_hours_total,new_minutes_total,new_seconds_total]
                print(f"updated: {rows[i]}")
                break

        else:
            new_hours, new_minutes, new_seconds = calculate_time_parts(round(time_passed))
            rows.append([date_today, new_hours, new_minutes, new_seconds])
            print(f"appended: {[date_today, new_hours, new_minutes, new_seconds]}")

        with open(log_file, "w") as file:
            csv.writer(file).writerows(rows)

        last_activity = time.time()
        activity_detected = False
