tempratures = [30.23, 26.73, 29.45, 17.93, 20.76, -2.23]

avg_temp = sum(tempratures)/ len(tempratures)
baseline_temp = 18
print(f"average temprature: {avg_temp:.2f}°C")
if avg_temp > 25 :
    print("you are iin for a long and hot day")

if avg_temp >= baseline_temp <= avg_temp:
    print("this is the perfect weather!!!!!")
if avg_temp < baseline_temp:
    print ("its cold too cold ")