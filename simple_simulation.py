import math
# ____the GOOD ENOUGH MODEL____ 

Ballspeed = float(input(f"Ball Speed: "))

Launchangle = float(input(f"launch angle: "))*(math.pi/180) #into radians

backspin = float(input(f"Backspin: ")) *((2* math.pi) / 60) #into rad/s

x_velocity = math.cos(Launchangle) * Ballspeed
y_velocity = math.sin(Launchangle) * Ballspeed

# Constant Santiniack
rho = 1.225 #density of the air at sea level
mu = 1.81 * math.pow(10, -5) #dynamic Viscosity of the air
D = 0.04267 #Diameter of the golf ball
Afront = (math.pi * math.pow(D, 2)) / 4
Cd = 0
mass = 0.04593
area = (D/2)**2 * math.pi
DeltaT = 0.001
x_position = 0
y_position = 0.0000001
Decayrate = 0.0005
G = 9.81

while y_position >= 0: 

  mag_velocity = math.sqrt(math.pow(x_velocity, 2) + math.pow(y_velocity, 2)) 

  #MR.REYNOLDS

  re = (rho * mag_velocity * D) / mu

  if re < 1:
    
     Cd = 24 / re #stokes flow

  if 1 <= re <= (2 * math.pow(10,4)):

     Cd = 0.5

  if (2 * math.pow(10,4)) < re <=(8 * math.pow(10,4)):

     Cd = 0.22 -(0.000002 * (re - (2 * math.pow(10, 4))))

  if (8 * math.pow(10,4)) < re <= (3 * math.pow(10, 5)):
      
      Cd = 0.2

  S = (backspin *(D /2)) / mag_velocity

  Cl = 0.0504 + 1.2031*S - 1.1490*S**2

  Faero =  0.5 * rho * area * mag_velocity**2
  Df = Faero * Cd
  Lf = Faero * Cl

  alpha = math.atan2(y_velocity, x_velocity)

  Ax = (1 / mass) *(-Df * math.cos(alpha)- Lf * math.sin(alpha))
  Ay = (1 / mass) *(-Df * math.sin(alpha) - Lf * math.cos(alpha)) - G
  
  x_velocity = x_velocity + (Ax * DeltaT)
  y_velocity = y_velocity + (Ay * DeltaT)

  x_position = x_position + (x_velocity * DeltaT)
  y_position = y_position + (y_velocity * DeltaT)

  

  backspin = backspin * (1 - Decayrate * DeltaT)


print(f"X position: {x_position}")


