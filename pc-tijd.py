import time
import csv

#variabelen
last_activity = time.time()
file_obj = '/home/saartje/exe/programmeren/python/pc_tijd_loggen/pc_tijd_logggen.csv'

#hoofd loop
while True:
    user_input = input("meet activiteit...")

    current_time = time.time()
    time_passed = current_time - last_activity

    print(round(time_passed))

    if time_passed > 5:

        with open(file_obj, "r") as file:
            rows = list(csv.reader(file))

        for i, row in enumerate(rows):
            if time.strftime("%Y_%m_%d") in row[0]:
                oude_activiteit = float(row[1])
                nieuwe_activiteit = oude_activiteit + time_passed
                rows[i][1] = str(round(nieuwe_activiteit))

                print("oude activiteit ge-update")
                last_activity = time.time()
                break

        else:
            nieuwe_line = time.strftime("%Y_%m_%d") + " " + str(round(time_passed)) + "\n"

            with open("/home/saartje/exe/programmeren/python/pc_tijd_loggen/pc_tijd_logggen.txt", "a") as file:
                file.write(nieuwe_line)

            print(nieuwe_line)
            last_activity = time.time()
