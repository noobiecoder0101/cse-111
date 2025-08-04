import time 
import math
import datetime

today = datetime.date.today()

print("hello there")
tire_width = int(input("please input the tire's width in (milimeters)(ex 203): "))
tire_aspectr = int(input("please enter the aspect ratio of the tire(ex 30): "))
tire_diameter = int(input("please input the tire diameter in inches (ex 13): "))
tire_volume = (math.pi * tire_width**2 * tire_aspectr * (tire_width * tire_aspectr + 2540 * tire_diameter)) / 10000000000
tire_volume_2 = round(tire_volume, 2)
time.sleep(5)

print(f"the aproximate volume is {tire_volume:.2f}")



with open("volumes.txt", "a") as file_object:
    file_object.write(f"the day is: {today}, the tire width is: {tire_width}, the tire aspect ratio is: {tire_aspectr},  the tire diameter is: {tire_diameter}, the approximate tire volume is:{tire_volume_2} \n ")
# thank you message 

print("thank you for your time ")