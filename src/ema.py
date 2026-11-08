import numpy as np
def calculate_ema(prices, period):
    prices = np.asarray(prices, dtype=float)
    if period < 1:
        raise ValueError("Period must be positive")
    if prices.ndim != 1:
        raise ValueError("Prices must be a 1D array")
    if len(prices)<period:
        raise ValueError("Insufficient price data")
    if not np.all(np.isfinite(prices)):
        raise ValueError("Prices must contain finite values")
    # Calculating alpha
    alpha = 2/(period+1)
    ema = np.full(len(prices), np.nan)
    # SMA initialisation
    ema[period-1]=np.mean(prices[:period])
    # Recursive EMA calculation
    for t in range(period, len(prices)):
        ema[t]=alpha*prices[t]+(1-alpha)*ema[t-1]
    return ema