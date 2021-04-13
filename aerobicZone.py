"""

Zachary Montague
3/29/2021
Program to measure aerobic training zone

"""

# Request for user input
print("Welcome to the Aerobic Zone!")
age = int(input("Enter your age: "))
resting_heart_rate = int(input("Enter your resting heart rate: "))

# Calculations
heart_rate_reserve = (220 - age) - resting_heart_rate
low_end_fat_burning = heart_rate_reserve * 0.50 + resting_heart_rate
high_end_fat_burning = heart_rate_reserve * 0.75 + resting_heart_rate

# Display of results
print("Your heart rate reserve is ", heart_rate_reserve)
print("Your aerobic training zone is between ", low_end_fat_burning, " and ", high_end_fat_burning, "beats per minute")
