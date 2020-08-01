# Wersja 1 - na podstawie aktualnego czasu systemowego
"""import datetime

h = datetime.datetime.now().strftime("%H")
m = datetime.datetime.now().strftime("%M")
current_time = h+m

if (int(current_time) > 1800) or (int(current_time) < 600):
    print("I don't see the sun!")

else:
    if (int(current_time) < 1200):
        angle = (1200-int(current_time))*0.25
        print(angle)
    else:
        angle = (int(current_time)-1200)*0.25
        print(angle)"""

# Wersja 2 - wersja w której podajesz określoną godzinę
time = "05:55"


def timeToMinutes(time):
    hours = int(time[0] + time[1])
    minutes = int(time[3] + time[4])
    current_time_minutes = (hours * 60) + minutes
    return current_time_minutes


if (timeToMinutes(time) < 360) or (timeToMinutes(time) > 1080):
    print("I don't see the sun!")
    #na stronie w tym miejscu musi byc uzyta komenda return, nie print
else:
    if timeToMinutes(time) <= 720:
        sun_angle = (timeToMinutes(time)-360)*0.25
        print("Obecny kąt padania promieni Słonecznych wynosi: " + str(sun_angle))

    if timeToMinutes(time) > 720:
        sun_angle = (timeToMinutes(time)-360)*0.25
        print("Obecny kąt padania promieni Słonecznych wynosi: " + str(sun_angle))
