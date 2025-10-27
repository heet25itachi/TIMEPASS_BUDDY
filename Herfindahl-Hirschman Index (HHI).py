import numpy as np

def calculate_hhi(market_shares):
    """
    Calculates the Herfindahl-Hirschman Index (HHI) for market concentration.

    The HHI is calculated by summing the squares of the market shares 
    (expressed as percentages, not decimals) of all firms in the market.

    Formula: HHI = sum(s_i^2) where s_i is the market share of firm i.

    Args:
        market_shares (list or numpy array): A list of market shares. 
                                            These can be raw values (e.g., total 
                                            deposits) or percentages.

    Returns:
        float: The Herfindahl-Hirschman Index value.
    """
    
    if not market_shares:
        return 0.0

    # Convert to a NumPy array for easier calculation
    shares_array = np.array(market_shares, dtype=float)

    # 1. Normalize the shares to percentages (if not already percentages)
    # The HHI requires shares to be expressed as a percentage (e.g., 20 instead of 0.20)
    total_market_size = np.sum(shares_array)
    
    if total_market_size == 0:
        return 0.0
        
    # Calculate percentage shares
    percentage_shares = (shares_array / total_market_size) * 100

    # 2. Square each percentage share
    squared_shares = percentage_shares ** 2

    # 3. Sum the squared shares
    hhi = np.sum(squared_shares)

    return hhi

if __name__ == "__main__":
    # --- Example Usage: Banking Concentration in a Fictional Market ---
    
    # Raw data: Total assets/deposits (in billions) for 5 banks
    # Bank A: 40, Bank B: 30, Bank C: 15, Bank D: 10, Bank E: 5
    # Total Market Size = 40 + 30 + 15 + 10 + 5 = 100 billion
    
    # Corresponding Market Shares (in percentage):
    # Bank A: 40%, B: 30%, C: 15%, D: 10%, E: 5%

    BANK_ASSETS_BILLIONS = [40, 30, 15, 10, 5]

    # Calculate the HHI
    hhi_value = calculate_hhi(BANK_ASSETS_BILLIONS)

    # --- Interpretation Guide ---
    # HHI < 1,500: Unconcentrated market
    # 1,500 < HHI < 2,500: Moderately concentrated
    # HHI > 2,500: Highly concentrated

    print("--- Market Concentration Analysis (HHI) ---")
    print(f"Bank Asset Data (Billions): {BANK_ASSETS_BILLIONS}")
    print("-" * 45)
    print(f"Calculated Herfindahl-Hirschman Index (HHI): {hhi_value:.2f}")

    # Calculate the interpretation based on the standard US Department of Justice guidelines
    if hhi_value < 1500:
        concentration_level = "Unconcentrated"
    elif hhi_value <= 2500:
        concentration_level = "Moderately Concentrated"
    else:
        concentration_level = "Highly Concentrated"
        
    print(f"Market Concentration Level: {concentration_level}")
