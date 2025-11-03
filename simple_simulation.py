import math

def simulate_trajectory(speed, angle_deg, spin_rpm, cd_value, cl_value=0.3):
    """Simulate golf ball trajectory and return carry distance and peak height"""
    theta = math.radians(angle_deg)
    spin = ((2 * math.pi)/60) * spin_rpm
    
    Vxo = math.cos(theta) * speed
    Vyo = math.sin(theta) * speed
    
    # Constants
    mass = 0.04593
    D = 0.04267
    time = 0.0001
    a = math.pi * ((D / 2)**2)
    rho = 1.225
    x = 0
    y = 0
    max_height = 0
    
    while y >= 0:
        mag_velocity = math.sqrt(Vxo**2 + Vyo**2)
        theta = math.atan2(Vyo, Vxo)
        
        Fd = 0.5 * cd_value * a * rho * mag_velocity**2
        Fm = 0.5 * cl_value * a * rho * mag_velocity**2
        
        Fdx = -Fd * math.cos(theta)
        Fdy = -Fd * math.sin(theta)
        
        Fmx = -Fm * math.sin(theta) * (spin / abs(spin) if spin != 0 else 0)
        Fmy = Fm * math.cos(theta) * (spin / abs(spin) if spin != 0 else 0)
        
        Ftotal_x = Fdx + Fmx
        Ftotal_y = Fdy + Fmy - (mass * 9.81)
        
        ax = Ftotal_x / mass
        ay = Ftotal_y / mass
        
        Vxf = Vxo + ax * time
        Vyf = Vyo + ay * time
        
        x += Vxo * time
        y += Vyo * time
        
        if y > max_height:
            max_height = y
        
        Vxo = Vxf
        Vyo = Vyf
    
    return x, max_height

# Input parameters
mag_velocity = float(input(f"Speed: "))
angle = float(input(f"Degrees: "))
spin_rate = float(input(f"Spin rate (RPM): "))

# Single simulation with current values
cl = 0.3
cd = 0.25

carry, peak = simulate_trajectory(mag_velocity, angle, spin_rate, cd, cl)
print(f"\nCurrent simulation (cd={cd}, cl={cl}):")
print(f"Range: {carry:.2f} m")
print(f"Peak height: {peak:.2f} m")

# Test all combinations of cd and cl (both 0.05 to 1.5)
print(f"\n\nTesting all cd (0.05-1.50) and cl (0.05-1.50) combinations:\n")

for cd_test in [i * 0.05 for i in range(1, 31)]:  # 0.05 to 1.50 in steps of 0.05
    print(f"\n--- cd = {cd_test:.2f} ---")
    print(f"{'cl':<8} {'Carry (m)':<12} {'Peak Height (m)':<15}")
    print("-" * 40)
    
    for cl_test in [i * 0.05 for i in range(1, 31)]:  # 0.05 to 1.50 in steps of 0.05
        carry_test, peak_test = simulate_trajectory(mag_velocity, angle, spin_rate, cd_test, cl_test)
        print(f"{cl_test:<8.2f} {carry_test:<12.2f} {peak_test:<15.2f}")
