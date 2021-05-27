import time
print("The time what shall i remind you ?")
text=str(input())
print("In how many minutes?")
local_time=float(input())
local_time=local_time*60
time.sleep(local_time)
print(text)
