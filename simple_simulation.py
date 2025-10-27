import math

# ----------- Variables ----------- #
Ball_Speed = float(input("Enter Ball Speed (m/s): "))

# Convert degrees to radians
Launch_Angle = float(input("Enter Launch Angle (degrees): ")) * (math.pi/180)

# Backspin is usually in RPM, but your simplified model uses rad/s for 'S' calculation.
# Assuming input is in RPM and converting to rad/s for consistency with physics models.
BackSpin_RPM = float(input("Enter Backspin rate (RPM): "))
Initial_Omega = BackSpin_RPM * (2 * math.pi / 60) # Convert RPM to rad/s

# --- Simple Projectile Motion (No Air Resistance) ---
Initial_Y_Velocity = (Ball_Speed * math.sin(Launch_Angle))
print(f"Initial Y Velocity = {Initial_Y_Velocity:.2f} m/s")

Initial_X_Velocity = (Ball_Speed * math.cos(Launch_Angle))
print(f"Initial X Velocity = {Initial_X_Velocity:.2f} m/s")

# Gravity (g) is 9.81 m/s^2, 2g is 19.62
Peak_Height_No_Air = Initial_Y_Velocity**2 / (2 * 9.81)
print(f"Peak Height (No Air) = {Peak_Height_No_Air:.2f} meters")

# Time of flight is 2 * (time to apex)
Time_No_Air = (Initial_Y_Velocity / 9.81) * 2
print(f"Time of Flight (No Air) = {Time_No_Air:.2f} seconds")

Carry_Distance_No_Air = (Initial_X_Velocity * Time_No_Air)
print(f"Carry Distance (No Air) = {Carry_Distance_No_Air:.2f} meters")

print("-" * 30)
print("SIMULATION WITH AIR RESISTANCE:")

# --- Numerical Integration Setup ---
# Initialize dynamic variables for the simulation
vx = Initial_X_Velocity
vy = Initial_Y_Velocity
x = 0.0
y = 0.000001 # Start slightly above zero to enter the loop
max_height = 0.0
current_omega = Initial_Omega # Current angular velocity (rad/s)

# CONSTANTS
DeltaT = 0.001 # Reduced time step for better accuracy
Mass = 0.04593 # kg
Radius = 0.0213 # m
Gravity = -9.81 # m/s^2
rho = 1.225 # Air density (kg/m^3) at sea level
Area = math.pi * Radius**2

# SIMPLIFIED MODEL FOR COEFICIENTS
Cdbase = 0.25
Cdfactor = 0.0025
Clfactor = 3
Decayrate = 0.0005 # Spin decay rate

# --- Simulation Loop (Euler's Method) ---
while y >= 0:
    # Store current position for final carry distance if y goes negative
    x_prev = x
    y_prev = y

    # 1. Calculate Forces
    mag_velocity = math.sqrt(vx**2 + vy**2)

    # Prevent division by zero if mag_velocity is zero
    if mag_velocity == 0:
        break 

    # Spin Ratio (S): ratio of ball surface speed to flight speed
    S = (Radius * current_omega) / mag_velocity

    # Calculate Coefficients
    Cdf = Cdbase + (Cdfactor * S)
    Clf = Clfactor * S

    # Calculate Force Magnitudes
    Faero = 0.5 * rho * Area * mag_velocity**2
    Df = Faero * Cdf # Drag Force
    Lf = Faero * Clf # Lift Force (Magnus)

    # 2. Acceleration Components
    # Use math.atan2(vy, vx) to get the correct angle (alpha) in all quadrants
    alpha = math.atan2(vy, vx)
    
    # Horizontal Acceleration (Drag and Lift components oppose forward motion)
    Ax = (1 / Mass) * (-Df * math.cos(alpha) - Lf * math.sin(alpha))
    
    # Vertical Acceleration (Gravity down, Drag opposes motion, Lift up)
    Ay = (1 / Mass) * (Mass * Gravity - Df * math.sin(alpha) + Lf * math.cos(alpha))

    # 3. Update Velocity
    vx_new = vx + (Ax * DeltaT)
    vy_new = vy + (Ay * DeltaT)

    # 4. Update Position (using new velocities for slightly better integration, or old for pure Euler)
    # Using old velocities for pure Euler integration:
    x_new = x + (vx * DeltaT)
    y_new = y + (vy * DeltaT)
    
    # 5. Update Spin Decay
    current_omega = current_omega * (1 - Decayrate * DeltaT)
    
    # 6. Update State Variables for Next Step
    vx = vx_new
    vy = vy_new
    x = x_new
    y = y_new

    # 7. Track Peak Height
    max_height = max(max_height, y)
    
# --- Final Results ---
# When the loop breaks (y <= 0), the final carry distance is x.
Carry_Distance_Meters = x

print(f"Calculated Carry Distance (Air) = {Carry_Distance_Meters:.2f} meters")
print(f"Calculated Peak Height (Air) = {max_height:.2f} meters")
print("-" * 30)

print(f"Carry with air resistance and spin: {New_X_Position}")



