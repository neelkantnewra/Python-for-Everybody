# Difference in two time stamp HH:MM:AM/PM  time in minute

# Author: Neelkant Newra
#github: https://github.com/neelkantnewra

def StringChallenge(strParam):
    Time = list(strParam.split("-"))
    Start_time = convert(Time[0])
    End_time = convert(Time[1])
    
    if Start_time>End_time:
        End_time += 1440
    strParam = End_time - Start_time
    return strParam

def convert(time):
    time_hrs = time.split(":")[0]
    time_min = time.split(":")[1][:2]
    timeap =  time.split(":")[1][2:]
    if timeap == "am":
        if time_hrs == "12":
            time_hrs = "00"
    elif time_hrs != 12:
        time_hrs = str(int(time_hrs)+12)
    return int(time_hrs)* 60 + int(time_min)
  
print(StringChallenge(input()))   
