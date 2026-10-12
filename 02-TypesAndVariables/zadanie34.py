###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600
speed_ms = round(speed_ms, 2)
print(speed_kmh, "km/h = ", speed_ms, "m/s")
