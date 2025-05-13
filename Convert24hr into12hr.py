currenthr = int(input("Enter hour (0-23): "))
currentmin = int(input("Enter minute (0-59 or more): "))

# Normalize minutes
currenthr += currentmin // 60
currentmin = currentmin % 60

# Normalize hours to 24-hour format
currenthr = currenthr % 24

# Determine period
period = "AM"
if currenthr >= 12:
    period = "PM"

# Convert to 12-hour format
newhr = currenthr % 12
if newhr == 0:
    newhr = 12

print(f"The time is {newhr} hr and {currentmin} min {period}")
