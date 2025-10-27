import numpy as np

def macaulay_duration(cash_flows, times, ytm):
    """
    Calculates the Macaulay Duration of a bond or financial instrument.

    The formula used is:
    MacD = (Sum_{i=1}^{n} t_i * PV_i) / (Sum_{i=1}^{n} PV_i)

    Where:
    - t_i is the time until the i-th cash flow.
    - PV_i is the Present Value of the i-th cash flow: PV_i = C_i / (1 + ytm)^t_i
    - ytm is the yield to maturity (or discount rate) per period.

    Args:
        cash_flows (list or numpy array): List of cash flow amounts (coupon payments 
                                          and final principal payment).
        times (list or numpy array): List of time periods (in years) corresponding 
                                     to the cash flows. Must be the same length 
                                     as cash_flows.
        ytm (float): The yield to maturity, expressed as a decimal (e.g., 0.05 for 5%).

    Returns:
        float: The Macaulay Duration in years.
    """

    if len(cash_flows) != len(times):
        # Corrected typo in 'sameb' to 'same'
        raise ValueError("The 'cash_flows' and 'times' arrays must have the same length.")

    # 1. Calculate the Present Value (PV_i) for each cash flow
    # PV_i = C_i / (1 + ytm)^t_i
    present_values = [] # Standardized to 'present_values'
    for cf, t in zip(cash_flows, times):
        pv = cf / ((1 + ytm) ** t)
        present_values.append(pv) # Corrected typo: 'present_values_append(pv)'

    # Convert lists to NumPy arrays for easy element-wise multiplication
    pv_array = np.array(present_values)
    times_array = np.array(times)

    # 2. Calculate the total Present Value of the bond (V) - the denominator
    # V = Sum_{i=1}^{n} PV_i
    total_present_value = np.sum(pv_array)

    # Handle the case where total_present_value is zero to avoid division by zero
    if total_present_value == 0:
        return 0.0

    # 3. Calculate the weighted present value components (t_i * PV_i) - Numerator components
    # NOTE: Swapped order with step 4 to ensure 'weighted_pv_components' is defined before use
    weighted_pv_components = times_array * pv_array

    # 4. Calculate the sum of the weighted present value - the numerator
    # Numerator: Sum_{i=1}^{n} t_i * PV_i
    sum_weighted_pv = np.sum(weighted_pv_components)

    # 5. Calculate Macaulay Duration
    # MacD = Numerator / Denominator
    macd = sum_weighted_pv / total_present_value

    return macd

if __name__ == "__main__":
    # --- Example Usage ---

    # Example: 3-year bond, $1000 face value, 8% annual coupon, YTM of 10%

    # Cash Flows (Coupon for Year 1, Coupon for Year 2, Coupon + Principal for year 3)
    CASH_FLOWS = [80.0, 80.0, 1080.0]

    # Times (in years)
    TIMES = [1.0, 2.0, 3.0]

    # Yield to Maturity (10% expressed as a decimal)
    YTM = 0.10

    # Calculate the Macaulay Duration
    try:
        duration = macaulay_duration(CASH_FLOWS, TIMES, YTM)

        # Print the results
        print(f"--- Bond Data ---")
        # Corrected typo: 'CAHS_FLOWS' to 'CASH_FLOWS'
        print(f"Cash Flows: {CASH_FLOWS}")
        print(f"Payment Times: {TIMES} years")
        # Corrected typo/style: removed space in format specifier ':. 2f' -> ':.2f'
        print(f"YTM: {YTM * 100:.2f}%")
        print("-" * 25)
        print(f"Calculated Macaulay Duration (MacD): {duration:.4f} years")

        # Expected result for validation: ~ 2.7766 years
        print(f"Interpretation: This is the weighted average time until the bond's cash flows are received.")
        
    except ValueError as e:
        print(f"Error: {e}")

