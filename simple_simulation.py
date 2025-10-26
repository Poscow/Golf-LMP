import math


# ----------- Variables ----------- # 
Ball_Speed = float(input("Enter Ball Speed: "))

Launch_Angle = float(input("Enter Launch Angle: ")) * (math.pi/180)

Initial_Y_Velocity = (Ball_Speed * math.sin(Launch_Angle))
print(f"Initial Y Velocity = {Initial_Y_Velocity}")

Initial_X_Velocity = (Ball_Speed * math.cos(Launch_Angle))
print(f"Initial X Velocity = {Initial_X_Velocity}")

Initial_Y_Velocity_Sqaured = math.pow(Initial_Y_Velocity, 2)

Peak_Height = Initial_Y_Velocity_Sqaured / 19.62 
print(f"Peak Height = {Peak_Height}")

Time = (Initial_Y_Velocity / 9.81) * 2
print(f"Time Took was: {Time}")

Carry_Distance_Meters = (Initial_X_Velocity * Time)
print(f"Carry Distance = {Carry_Distance_Meters}")

print("WITH AIR RESISTANCE:")
New_Time = Time * 100

New_X_Velocity = Initial_X_Velocity
New_Y_Velocity = Initial_Y_Velocity

#CONSTANTS
Timeint = 0.1
Mass = 0.04593
Gravity = -9.81
rho = 1.225 #at sea level
X_Position = 0
Y_Position = 0 
New_X_Position = X_Position
New_Y_Position = Y_Position
Cd_Count = 0 

while Cd_Count < New_Time:
    Cd = 0.5 * math.e ** (-0.00465 * (Cd_Count - 1))

    Mag_Velocity = math.sqrt((New_X_Velocity ** (2)) + (New_Y_Velocity ** (2)))

    Fd = -1 * (0.5 * rho * (Mag_Velocity ** (2)) * Cd * 0.001429406186)
    
    Fdx = Fd * (New_X_Velocity/Mag_Velocity)
    Fdy = Fd * (New_Y_Velocity/Mag_Velocity)

    Fg = Mass * Gravity

    Fnetx = Fdx
    Fnety = Fg + Fdy

    Ax = Fnetx/Mass
    Ay = Fnety/Mass

    #update position
    New_X_Position = New_X_Position + (New_X_Velocity * Timeint)
    print(f"{New_X_Position}")
    New_Y_Position = New_Y_Position + (New_Y_Velocity * Timeint)
    print(f"{New_Y_Position}")
    #update velocity
    New_X_Velocity = New_X_Velocity + (Ax * Timeint)
    New_Y_Velocity = New_Y_Velocity + (Ay * Timeint)

    Cd_Count += 1 


