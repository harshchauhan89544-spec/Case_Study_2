# Temperature Monitoring System
# Name: Harsh Chauhan
# Roll No: 202501100700076

import random
import time

# Take minimum and maximum temperature from user
min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

print("\nTemperature Monitoring Started...\n")

while True:
    # Generate random temperature between 0 and 100
    temperature = random.randint(0, 200)
    
    print("Current Temperature:", temperature)

    # Compare temperature with limits
    if temperature > max_temp:
        print("Alert: Temperature is too high")
    elif temperature < min_temp:
        print("Alert: Temperature is too low")
    else:
        print("Temperature is within acceptable limit")
    
    print("-------------------------------")
    
    # Wait for 2 seconds
    time.sleep(2)