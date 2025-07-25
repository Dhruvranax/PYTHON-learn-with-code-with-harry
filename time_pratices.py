import time

# Step 1: Get current hour, minute, second
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

# Optional: Display full timestamp
print(f"Current Time: {hour}:{minute}:{second}")

# Step 2: Stay with if-elif-else — no fancy changes
if hour >= 4 and hour < 12:
    print("Good Morning 😊")

elif hour >= 12 and hour < 17:
    print("Good Afternoon 👩‍💻")

elif hour >= 17 and hour < 21:
    print("Good Evening 👋")

else:
    print("Good Night 😴")

#  for more information about time please visit this website.
#  https://docs.python.org/3/library/time.html#time.strftime