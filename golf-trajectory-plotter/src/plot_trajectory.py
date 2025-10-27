import matplotlib.pyplot as plt
import numpy as np

# Function to simulate the trajectory of the golf ball
def simulate_trajectory(ball_speed, launch_angle_deg, backspin_rpm):
    import math

    # Convert units
    launch_angle = math.radians(launch_angle_deg)
    omega0 = backspin_rpm * (2 * math.pi / 60.0)  # rad/s

    # Physical constants / model parameters (reasonable defaults)
    m = 0.04593           # kg (mass of golf ball)
    R = 0.021335          # m (radius ~ 42.67 mm diameter)
    A = math.pi * R * R   # cross-sectional area
    rho = 1.225           # kg/m^3 air density
    g = -9.81             # m/s^2
    mu_air = 1.81e-5      # Pa*s (dynamic viscosity of air)
    decay_rate = 0.0006   # spin decay per second (simple exponential-ish)
    dt = 0.001            # time step (s)

    # Coefficient parameters (empirical-ish)
    Cd_low = 0.47         # high Cd for low Re (smooth sphere)
    Cd_high = 0.20        # low Cd for turbulent/dimpled golf ball
    Cl_spin_factor = 1.2  # scale factor to convert spin ratio S -> Cl
    Cd_spin_sensitivity = 0.0025  # small effect of spin on Cd

    # Initial velocities
    vx = ball_speed * math.cos(launch_angle)
    vy = ball_speed * math.sin(launch_angle)

    # Numerical integration (2D) with aerodynamic drag + Magnus (lift from backspin)
    x = 0.0
    y = 0.000001  # tiny start above ground to allow loop
    omega = omega0
    time = 0.0
    heights = []
    distances = []

    while True:
        v = math.hypot(vx, vy)
        if v < 1e-8:
            break

        # Reynolds number and dynamic Cd estimate
        D = 2 * R
        Re = rho * v * D / mu_air
        Cd = Cd_high + (Cd_low - Cd_high) * math.exp(-((Re / 1.5e5)**2))
        S = (R * omega) / v
        Cd += Cd_spin_sensitivity * abs(S)

        Cl = (Cl_spin_factor * S) / (1.0 + 4.0 * abs(S))

        q = 0.5 * rho * v * v
        Dforce = q * A * Cd
        Lforce = q * A * Cl

        ux, uy = vx / v, vy / v
        nx, ny = -uy, ux

        ax = (-Dforce * ux + Lforce * nx) / m
        ay = (m * g - Dforce * uy + Lforce * ny) / m

        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        time += dt

        omega *= (1.0 - decay_rate * dt)

        heights.append(y * 3.28084)  # Convert to feet
        distances.append(x * 1.0936133)  # Convert to yards

        if y <= 0.0:
            break

    return distances, heights

# Main function to plot the trajectory
def main():
    ball_speed = float(input("Enter Ball Speed (m/s): "))
    launch_angle_deg = float(input("Enter Launch Angle (degrees): "))
    backspin_rpm = float(input("Enter Backspin rate (RPM): "))

    distances, heights = simulate_trajectory(ball_speed, launch_angle_deg, backspin_rpm)

    plt.figure(figsize=(10, 5))
    plt.plot(distances, heights, label='Golf Ball Trajectory', color='green')
    plt.title('Golf Ball Trajectory')
    plt.xlabel('Distance (yards)')
    plt.ylabel('Height (feet)')
    plt.grid()
    plt.legend()
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.show()

if __name__ == "__main__":
    main()