import numpy as np

# Define fundamental constants
C_LIGHT = 299792458.0        # Speed of light (m/s)
E_MASS_KG = 9.10938356e-31   # Electron rest mass (kg)
E_CHARGE = 1.602176634e-19   # Elementary charge (C)
JOULES_PER_EV = 1.602176634e-19 # Conversion factor (J/eV)

# Convert electimportron rest mass to energy units (MeV)
# E = mc^2
E_REST_J = E_MASS_KG * C_LIGHT**2
E_REST_MEV = (E_REST_J / JOULES_PER_EV) / 1e6

# ----------------------------------------------------------------------
# Core Relativistic Calculations
# ----------------------------------------------------------------------

def calculate_relativistic_properties(energy_gev):
    """
    Calculates the Lorentz factor, speed, and momentum for an electron 
    given its total energy in Giga-electron Volts (GeV).

    Args:
        energy_gev (float): Total electron energy in GeV.

    Returns:
        dict: A dictionary containing gamma, speed (fraction of c), 
              and momentum (in MeV/c).
    """
    
    energy_mev = energy_gev * 1000.0
    
    # 1. Calculate the Lorentz Factor (gamma)
    # E = gamma * E_rest  =>  gamma = E / E_rest
    gamma = energy_mev / E_REST_MEV
    
    # 2. Calculate the Speed (as a fraction of c, beta = v/c)
    # gamma = 1 / sqrt(1 - beta^2)  =>  beta = sqrt(1 - 1/gamma^2)
    # For highly relativistic particles (gamma >> 1), beta is very close to 1.
    if gamma <= 1:
        # Handle non-relativistic or rest state
        beta = 0.0
    else:
        # Calculate beta using the relativistic formula
        beta = np.sqrt(1.0 - (1.0 / gamma**2))

    # 3. Calculate the Momentum (p)
    # p = gamma * m_e * v, often expressed as p = gamma * m_e * c * beta 
    # Momentum is usually expressed in units of MeV/c
    momentum_mevc = gamma * E_REST_MEV * beta
    
    return {
        "gamma": gamma,
        "beta": beta,
        "momentum_mevc": momentum_mevc
    }

# ----------------------------------------------------------------------
# Example Usage: Analyze a 10 GeV Electron Beam
# ----------------------------------------------------------------------

# The paper discusses acceleration up to 10 GeV
TARGET_ENERGY_GEV = 10.0

# Calculate the properties
properties = calculate_relativistic_properties(TARGET_ENERGY_GEV)

# Calculate the speed difference from c
speed_difference = (1.0 - properties["beta"]) * C_LIGHT

# Output the results
print("--- Analysis of a High-Energy Electron Beam (LWFA) ---")
print(f"Electron Rest Mass Energy ($m_e c^2$): {E_REST_MEV:.3f} MeV")
print(f"Target Electron Total Energy: {TARGET_ENERGY_GEV:.2f} GeV")
print("-" * 55)

print(f"1. Lorentz Factor ($\gamma$): {properties['gamma']:.0f}")
print(f"   (This shows the electron's mass/energy has increased by this factor)")
print(f"2. Speed ($v/c$): {properties['beta']:.12f}")
print(f"   (Extremely close to the speed of light, $c$)")
print(f"3. Momentum ($p$): {properties['momentum_mevc'] / 1000.0:.3f} GeV/c")
print("-" * 55)

print(f"4. Velocity Difference from $c$:")
print(f"   The electron's speed is {speed_difference:.2f} m/s slower than the speed of light ($c$).")
print(f"   (A highly relativistic particle's speed is effectively $c$ for most purposes)")

# Additional LWFA-related derived calculation (Plasma Wavelength Estimation)
# In LWFA, the accelerating structure is the plasma wakefield,
# which has a plasma wavelength related to the plasma density (n_e).
# For n_e = 1e18 cm^-3 (a typical LWFA density):
PLASMA_DENSITY_CM3 = 1e18
PLASMA_FREQUENCY = np.sqrt(PLASMA_DENSITY_CM3 * E_CHARGE**2 / (E_MASS_KG * 8.854e-12))
# The plasma wavelength is roughly: lambda_p ~ c / f_p
PLASMA_WAVELENGTH = (C_LIGHT / PLASMA_FREQUENCY) * 1e6 # in micrometers (μm)

print("\n--- Contextual Physics (Plasma Wakefield) ---")
print(f"Estimated Plasma Wavelength ($\lambda_p$) at $10^{18}$ cm$^{-3}$: {PLASMA_WAVELENGTH:.2f} $\mu$m")
print(f"   (This is the characteristic length scale of the accelerator structure)")
