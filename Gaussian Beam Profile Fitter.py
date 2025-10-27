import numpy as np
from scipy.optimize import curve_fit

# ----------------------------------------------------------------------
# 1. Define the Mathematical Model (Gaussian Function)
# ----------------------------------------------------------------------
def gaussian(x, amplitude, center_x, sigma):
    """
    A 1D Gaussian function used to model a beam profile.

    Parameters:
    - x: The position coordinate (e.g., transverse distance in mm).
    - amplitude: The peak intensity of the beam (A).
    - center_x: The horizontal or vertical center of the beam (mu).
    - sigma: The standard deviation, related to the beam spot size (sigma).
    """
    return amplitude * np.exp(-((x - center_x) ** 2) / (2 * sigma ** 2))

# ----------------------------------------------------------------------
# 2. Generate Mock Experimental Data (Simulate a Muon Beam Profile)
# ----------------------------------------------------------------------
# True parameters for the simulated beam
TRUE_AMPLITUDE = 100.0   # Maximum muon count
TRUE_CENTER = 5.0        # Beam center at 5.0 mm
TRUE_SIGMA = 1.2         # Beam width/spot size (1.2 mm standard deviation)

# Create 50 measurement points (e.g., positions on a detector screen)
x_data = np.linspace(0, 10, 50)

# Generate the theoretical intensity data
y_theoretical = gaussian(x_data, TRUE_AMPLITUDE, TRUE_CENTER, TRUE_SIGMA)

# Add random noise to simulate experimental measurement error
NOISE_LEVEL = 5.0
y_data = y_theoretical + NOISE_LEVEL * np.random.normal(size=x_data.size)

# ----------------------------------------------------------------------
# 3. Perform the Non-linear Curve Fitting
# ----------------------------------------------------------------------

# Set initial guesses for the parameters (critical for good fit convergence)
# Guess for amplitude: Max value in measured data
# Guess for center: Midpoint of the x-range
# Guess for sigma: A reasonable small positive value
initial_guesses = [np.max(y_data), np.mean(x_data), 1.0]

try:
    # Use curve_fit to find the optimal parameters (popt) and covariance (pcov)
    popt, pcov = curve_fit(gaussian, x_data, y_data, p0=initial_guesses)

    # Extract the fitted parameters
    fitted_amplitude, fitted_center, fitted_sigma = popt

    # Calculate the standard error (uncertainty) for each parameter from the covariance matrix
    perr = np.sqrt(np.diag(pcov))
    err_amplitude, err_center, err_sigma = perr

    # ----------------------------------------------------------------------
    # 4. Display Results
    # ----------------------------------------------------------------------
    print("--- Muon Beam Profile Analysis (Gaussian Fit) ---")
    print(f"Total simulated data points: {len(x_data)}")
    print("-" * 50)

    print("Fitted Beam Parameters:")
    print(f"1. Amplitude (Peak Intensity): {fitted_amplitude:.2f} +/- {err_amplitude:.2f}")
    print(f"2. Center Position (Centroid): {fitted_center:.3f} mm +/- {err_center:.3f} mm")
    print(f"3. Beam Width (Sigma):       {fitted_sigma:.3f} mm +/- {err_sigma:.3f} mm")
    print("\nInterpretation:")
    print(f"The $\sigma$ (Sigma) parameter represents the standard deviation of the beam,")
    print(f"which is directly related to the beam spot size and its angular divergence.")

    # Note: To visualize the fit, you would typically use matplotlib here.
    # We will just print the final fit results.

except RuntimeError as e:
    print(f"Error: Optimal parameters were not found during fitting.")
    print(f"Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
