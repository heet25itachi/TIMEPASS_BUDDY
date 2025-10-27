import numpy as np

# Define constants
E_CHARGE = 1.602176634e-19    # Elementary charge (C)
E_MASS_KG = 9.10938356e-31    # Electron rest mass (kg)
EPSILON_0 = 8.854187817e-12   # Permittivity of free space (F/m)
C_LIGHT = 299792458.0         # Speed of light (m/s)

# ----------------------------------------------------------------------
# PART 1: Classical Space-Charge Limited Current (Child-Langmuir Law Analogue)
# This is a basic model to understand current limits in a diode-like system
# ----------------------------------------------------------------------

def calculate_space_charge_limit(voltage_v, distance_m, cathode_area_m2):
    """
    Calculates the maximum current (I_max) that can be extracted from a 
    cathode given a voltage and electrode spacing, based on a simplified 
    non-relativistic space-charge-limited flow model (Child-Langmuir).

    Formula (Approximation for a diode): I_max ~ K * V^(3/2) * Area / d^2

    Args:
        voltage_v (float): Applied voltage (V).
        distance_m (float): Distance between cathode and anode (m).
        cathode_area_m2 (float): Area of the cathode/emission (m^2).

    Returns:
        float: Maximum space-charge limited current in Amperes (A).
    """
    
    # Perveance constant K for electrons (simplified, non-relativistic, planar geometry)
    # K = (4/9) * epsilon_0 * (2*e/m_e)^(1/2) 
    perveance_constant_k = (4.0/9.0) * EPSILON_0 * np.sqrt(2 * E_CHARGE / E_MASS_KG)

    # Simplified current formula (Amperes)
    i_max = perveance_constant_k * (voltage_v ** 1.5) * (cathode_area_m2 / (distance_m ** 2))
    
    return i_max

# ----------------------------------------------------------------------
# PART 2: Basic Simulation of Transverse Space-Charge Expansion
# This models how a bunch radius grows over time due to mutual repulsion
# ----------------------------------------------------------------------

def simulate_transverse_expansion(initial_radius_m, initial_charge_c, gamma, z_points_m):
    """
    Simulates the transverse expansion of a particle bunch as it drifts
    due to space-charge forces (using a simplified linear model).

    This calculation is fundamental to optimizing the geometry for 
    creating the ellipsoidal bunches described in the paper.

    Args:
        initial_radius_m (float): Initial transverse bunch radius (m).
        initial_charge_c (float): Total bunch charge (C).
        gamma (float): Lorentz factor (relativistic factor) of the electrons.
        z_points_m (numpy.array): Distances (z-axis) along the drift space (m).

    Returns:
        numpy.array: The corresponding bunch radius (r) at each z-point (m).
    """
    
    # The expansion parameter (k) depends on charge, gamma, and initial radius
    # K is proportional to Q / (gamma^3 * r_0^2)
    # This factor governs the parabolic growth rate of the radius squared
    # A standard linear expansion formula for radius squared is often used: 
    # r^2(z) = r_0^2 + (k * z)^2

    # Simplified, non-linear constant related to the beam's perveance:
    # A more rigorous treatment requires solving the envelope equation, 
    # but for simplicity, we use an approximation based on the drift
    # space evolution of a uniform charge distribution (like the desired ellipsoid).
    # We define a 'growth rate constant' derived from the generalized perveance:
    
    # Factor relating to the current / perveance
    B = (2.0 * E_CHARGE) / (4.0 * np.pi * EPSILON_0 * E_MASS_KG * (C_LIGHT * gamma)**3)
    
    # Simplified growth rate constant (k_g) [m^-1]
    k_g = B * initial_charge_c / initial_radius_m**2 

    # Parabolic expansion of the bunch radius squared (r^2(z))
    # r(z) = r_0 * sqrt(1 + (k_g * z)^2)
    radius_expansion = initial_radius_m * np.sqrt(1.0 + (k_g * z_points_m)**2)
    
    return radius_expansion

# ----------------------------------------------------------------------
# Example USAGE
# ----------------------------------------------------------------------

# PART 1: Limit Calculation
VOLTAGE = 50000.0   # 50 kV applied voltage
DISTANCE = 0.05     # 5 cm spacing
AREA = 1e-4         # 1 cm^2 photocathode area
i_limit = calculate_space_charge_limit(VOLTAGE, DISTANCE, AREA)

print("--- Part 1: Space-Charge Limited Current (Simplified Diode) ---")
print(f"Voltage: {VOLTAGE/1000.0} kV, Gap: {DISTANCE*100} cm, Area: {AREA*10000.0:.2f} cm^2")
print(f"Maximum Current (I_max): {i_limit * 1000.0:.3f} mA")
print("-" * 65)

# PART 2: Expansion Simulation (Modeling the drift in the accelerator)
CHARGE = 100e-12       # 100 pC (Pico-Coulomb) bunch charge (High Charge)
R_INITIAL = 1e-3       # 1 mm initial radius
GAMMA = 20.0           # Lorentz Factor for a mildly relativistic beam (E ~ 10 MeV)
DRIFT_DISTANCE = 1.0   # 1 meter drift space

z_points = np.linspace(0, DRIFT_DISTANCE, 11) # Check radius every 10 cm
r_expansion = simulate_transverse_expansion(CHARGE, R_INITIAL, GAMMA, z_points)

print("--- Part 2: Transverse Bunch Radius Expansion Simulation ---")
print(f"Initial Charge (Q): {CHARGE*1e12:.0f} pC")
print(f"Initial Radius (R_0): {R_INITIAL*1000.0:.1f} mm")
print(f"Relativistic Factor ($\gamma$): {GAMMA:.1f}")
print("-" * 65)

print("Drift Distance (m) | Final Radius (mm)")
print("-------------------|------------------")
for z, r in zip(z_points, r_expansion):
    print(f"{z:.2f}               | {r*1000.0:.3f}")
    
print("\nInterpretation:")
print("The radius grows significantly due to space-charge effects. The paper's goal is to manage this expansion to achieve an optimal ellipsoidal shape and preserve beam quality (low emittance).")
