# ...existing code...
import math


# ----------- Variables ----------- # 
def user_input():
    Ball_Speed = float(input("Enter Ball Speed (m/s): "))
    Launch_Angle = float(input("Enter Launch Angle (degrees): ")) * (math.pi / 180)
    return Ball_Speed, Launch_Angle

def calculate_initial_y_velocity(Ball_Speed, Launch_Angle):
    Initial_Y_Velocity = (Ball_Speed * math.sin(Launch_Angle))
    print(f"Initial Y Velocity = {Initial_Y_Velocity:.3f} m/s")
    return Initial_Y_Velocity

def calculate_initial_x_velocity(Ball_Speed, Launch_Angle):
    Initial_X_Velocity = (Ball_Speed * math.cos(Launch_Angle))
    print(f"Initial X Velocity = {Initial_X_Velocity:.3f} m/s")
    return Initial_X_Velocity

def calculate_peak_height(Initial_Y_Velocity):
    Initial_Y_Velocity_Squared = math.pow(Initial_Y_Velocity, 2)
    print(f"Squared Y Velocity = {Initial_Y_Velocity_Squared:.3f}")
    
    Peak_Height = Initial_Y_Velocity_Squared / 19.62 
    print(f"Peak Height = {Peak_Height:.3f} m")
    return Peak_Height

def calculate_time(Initial_Y_Velocity):
    Time = (Initial_Y_Velocity / 9.81) * 2
    print(f"Time Took was: {Time:.3f} s")
    return Time

def calculate_distance(Initial_X_Velocity, Time):
    Carry_Distance_Meters = float(Initial_X_Velocity * Time)
    Carry_Distance_Yards = Carry_Distance_Meters * 1.0936133

    print(f"Carry Distance = {Carry_Distance_Meters:.3f} m")
    print(f"Carry Distance = {Carry_Distance_Yards:.3f} yd")
    return Carry_Distance_Meters, Carry_Distance_Yards

# ----------- Main Execution ----------- # 
def main():
    try:
        Ball_Speed, Launch_Angle = user_input()
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    Initial_Y_Velocity = calculate_initial_y_velocity(Ball_Speed, Launch_Angle)
    Initial_X_velocity = calculate_initial_x_velocity(Ball_Speed, Launch_Angle)
    Peak_Height = calculate_peak_height(Initial_Y_Velocity)
    Time = calculate_time(Initial_Y_Velocity)
    Carry_Distance_Meters, Carry_Distance_Yards = calculate_distance(Initial_X_velocity, Time)

    # summary
    print("\n--- Summary ---")
    print(f"Peak height: {Peak_Height:.3f} m")
    print(f"Time of flight: {Time:.3f} s")
    print(f"Carry: {Carry_Distance_Meters:.3f} m / {Carry_Distance_Yards:.3f} yd")


if __name__ == "__main__":
    main()
# ...existing code...
