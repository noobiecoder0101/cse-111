import datetime 

now = datetime.datetime.now()

# Get the day of the week as an integer (Monday is 0, Sunday is 6)
day_of_week_int = now.weekday()


print(f"{day_of_week_int}")

subtotal = float(input("what is the subtotal please: ").strip())

if day_of_week_int == 1 or day_of_week_int == 2:
    if subtotal >= 50:
        print("you are elegible for the discount ! ! ! ")
        discount = subtotal * 0.1
        print(f"your discount is :{discount}$")
        later_ammount = subtotal - discount
        print(f"your discounted total is :{later_ammount}")
        subtotal_ammount = later_ammount * 0.06
        total_ammount = subtotal_ammount + later_ammount
        print (f"total ammount : {total_ammount} ")
else:
    print("Sorry you do not qualify for the discount.")
