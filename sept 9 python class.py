distance = int(input("distance in miles? "))
actual_speed = int(input("what is your speed in miles per hour? "))
speed_limit = int(input("what is the average speed limit? "))

time_speed_limit = float(distance / speed_limit)
time_actual_speed = float(distance / actual_speed)
time_in_hour = 60

#time_save = (time_speed_limit - time_actual_speed)*60
#print("you save ", time_save, "minutes")


if actual_speed > speed_limit:
    time_save = int((time_speed_limit - time_actual_speed)*time_in_hour)
    print("you save", time_save, "minutes")
else:
    print("You are a safe driver, no time is saved")


