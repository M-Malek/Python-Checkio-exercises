data_time = "11.04.1812 01:01"

months = ["none", "January", "Ferbuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

day = str(int(data_time[0] + data_time[1]))
month = int(data_time[3]+data_time[4])
year = data_time[6]+data_time[7]+data_time[8]+data_time[9]
hours = str(int(data_time[11]+data_time[12]))
minutes = str(int(data_time[14]+data_time[15]))

if hours == "1":
    hours += " hour "
else:
    hours += " hours "

if minutes == "1":
    minutes += " minute"
else:
    minutes += " minutes"

actual_time = day + " " + str(months[month]) + " " + year + " year " + hours + minutes
print(actual_time)

if actual_time == "1 January 2020 year 0 hour 0 minutes":
    print(actual_time + " Millenium ")
else:
    print(actual_time)
