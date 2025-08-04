"""
When you physically exercise to strengthen your heart,
 you should maintain your 
heart rate within a range for at least 20 minutes.
 To find that range, subtract your age from 220.
 This difference is your maximum heart rate per minute.
   Your heart simply will not beat faster than this maximum 
(220 - age). When exercising to strengthen your heart, you should keep your
 heart rate between 65% and 85% of your heart’s maximum rate.


"""

age = int(input("how old are you"))
max_heart = 220 - age


part = 65
whole = 100 
percentage_1 = (part / whole ) * max_heart


part_2 = 85
percentage_2 = (part_2 / whole ) * max_heart


print(f"When you physically exercise to strengthen your heart, you should maintain your heart rate within a range of {percentage_1}BPM and {percentage_2}BPM for at least 20 minutes.")