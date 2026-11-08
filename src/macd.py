import numpy as np
from src.ema import calculate_ema
def calculate_macd(prices, fast=12, slow=26, signal_period=9):
    prices = np.asarray(prices, dtype=float)
    if fast < 1 or slow <= fast or signal_period < 1:
        raise ValueError("Invalid MACD parameters")
    if len(prices) < slow + signal_period - 1:
        raise ValueError("Insufficient price data for MACD")
    # Calculate fast and slow EMAs
    ema_fast=calculate_ema(prices, fast)
    ema_slow=calculate_ema(prices, slow)
    # MACD line
    macd=ema_fast-ema_slow
    # Signal line: EMA of valid MACD observations
    signal=np.full(len(prices), np.nan)
    first_valid=slow-1
    signal[first_valid:]=calculate_ema(macd[first_valid:], signal_period)
    # MACD histogram
    histogram = macd-signal
    return {
        "macd": macd,
        "signal": signal,
        "histogram": histogram
    }