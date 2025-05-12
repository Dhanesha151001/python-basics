#  Write a code where you calculate the time to reach from a location A - B when estimated time to travel is given


current_hour= int(input())
current_minute=int(input())
estimated_time_to_reach=int(input())

current_total_time_inmins= current_hour*60 + current_minute

arrival_time_in_mins = current_total_time_inmins + estimated_time_to_reach

print(f" Arrival time {arrival_time_in_mins}")

arrival_hour = (arrival_time_in_mins // 60) % 24 
arrival_minute = (arrival_time_in_mins % 60)  

print(f"The arrival hour is {arrival_hour}")
print(f"The arrival minute is {arrival_minute}")
