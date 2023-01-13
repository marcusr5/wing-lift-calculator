import math

# Altitude correction factor
def altitude_correction(altitude):
    """Calculate altitude correction factor"""
    return 1 - (2.2557 * 10**-5 * altitude)

# Temperature correction factor
def temperature_correction(temperature):
    """Calculate temperature correction factor"""
    return 1 - (0.0065 * temperature)

def calculate_lift(air_density, velocity, wing_area, angle_of_attack, aspect_ratio, sweep_angle, altitude, temperature):
    """Calculate lift using air density, velocity, wing area, angle of attack, aspect ratio, sweep angle, altitude and temperature"""
    
    #Calculating the dynamic pressure
    dynamic_pressure = (1/2) * air_density * (velocity**2)
    #calculating the lift coefficient
    lift_coefficient = (2*math.pi*angle_of_attack)/(math.cos(sweep_angle)+(aspect_ratio))
    #Calculating the lift 
    lift = dynamic_pressure * lift_coefficient * wing_area * altitude_correction(altitude) * temperature_correction(temperature)
    return lift

# Input air density, velocity, wing area, angle of attack, aspect ratio, sweep angle, altitude and temperature
air_density = float(input("Enter the air density (kg/m^3): "))
velocity = float(input("Enter the velocity of the aircraft (m/s): "))
wing_area = float(input("Enter the wing surface area (m^2): "))
angle_of_attack = float(input("Enter the angle of attack of the wing (degrees): "))
aspect_ratio = float(input("Enter the aspect ratio of the wing: "))
sweep_angle = float(input("Enter the sweep angle of the wing (degrees): "))
altitude = float(input("Enter the altitude of the aircraft (m): "))
temperature = float(input("Enter the temperature of the air (Celsius): "))

# Convert sweep angle to radians
sweep_angle = math.radians(sweep_angle)

# Calculate and output lift
lift = calculate_lift(air_density, velocity, wing_area, angle_of_attack, aspect_ratio, sweep_angle, altitude, temperature)
print("The lift of the wing is: ", lift, "N")
