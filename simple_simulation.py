import math


# ----------- Variables ----------- # 
Ball_Speed = float(input("Enter Ball Speed: "))

Launch_Angle = float(input("Enter Launch Angle: ")) * (math.pi / 180) #Launch angle is already turned in radians
    
Initial_Y_Velocity = (Ball_Speed * math.sin(Launch_Angle))

print(f"Initial Y Velocity = {Initial_Y_Velocity}")

Initial_Y_Velocity_Sqaured = math.pow(Initial_Y_Velocity, 2)

print(f"Squared Y Velocity = {Initial_Y_Velocity_Sqaured}")

Peak_Height = Initial_Y_Velocity_Sqaured / 19.62 

print(f"Peak Height = {Peak_Height}")

Time = (Initial_Y_Velocity / 9.81) * 2

print(f"Time Took was: {Time}")

Initial_X_Velocity = (Ball_Speed * math.cos(Launch_Angle))

print(f"Initial X Velocity = {Initial_X_Velocity}")

Carry_Distance_Meters = float(Initial_X_Velocity * Time)
Carry_Distance_Yards = int(Initial_X_Velocity * Time *3)

print(f"Carry Distance = {Carry_Distance_Meters}")

New_Time = Time * 100

Dc = math.e * (0.5) 

Cd_Count = 0

while Cd_Count <= New_Time:
    Cd_Count +=1

print(Cd_Count)
Dc_2 = Dc ** (-0.00465 * New_Time)
