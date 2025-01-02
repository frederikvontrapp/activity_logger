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

# variabelen
file_obj = '/home/saartje/exe/programmeren/python/pc_tijd_loggen/pc_tijd_logggen.csv'
activity_detected = False
last_activity= time.time()

# starten
keyboard.on_press(lambda _:log_activity())

# hoofd loop
while not activity_detected:
    time.sleep(0.1)

while activity_detected:
    user_input = input("meet activiteit...")

    current_time = time.time()
    time_passed = current_time - last_activity

    print(round(time_passed))

    if time_passed > 5:

        with open(file_obj, "r") as file:
            rows = list(csv.reader(file))

        for i, row in enumerate(rows):
            if len(row) < 4:
                continue

            if time.strftime("%Y_%m_%d") in row[0]:
                nieuwe_uren = round(time_passed) // 3600
                nieuwe_minuten = (round(time_passed) % 3600) // 60
                nieuwe_seconden = round(time_passed) % 60

                oude_uren = int(row[1])
                oude_minuten = int(row[2])
                oude_seconden = int(row[3])

                nieuwe_uren_totaal = nieuwe_uren + oude_uren + (nieuwe_minuten + oude_minuten) // 60
                nieuwe_minuten_totaal = (nieuwe_minuten + oude_minuten) % 60 + (nieuwe_seconden + oude_seconden) // 60
                nieuwe_seconden_totaal = (nieuwe_seconden + oude_seconden) % 60

                rows[i] = [time.strftime("%Y_%m_%d"),nieuwe_uren_totaal,nieuwe_minuten_totaal,nieuwe_seconden_totaal]

                with open(file_obj, "w") as file:
                    csv.writer(file).writerows(rows)

                print(rows[i])
                last_activity = time.time()
                break

        else:
            nieuwe_uren = round(time_passed) // 3600
            nieuwe_minuten = (round(time_passed) % 3600) // 60
            nieuwe_seconden = round(time_passed) % 60
            nieuwe_line = [time.strftime("%Y_%m_%d"),nieuwe_uren,nieuwe_minuten,nieuwe_seconden]

            with open(file_obj, "a") as file:
                csv.writer(file).writerow(nieuwe_line)

            print(nieuwe_line)
            last_activity = time.time()
