import numpy as np
def detect_crossovers(macd, signal):
    if len(macd) != len(signal):
        raise ValueError("Arrays must have equal lengths")
    bullish = np.zeros(len(macd), dtype=bool)
    bearish = np.zeros(len(macd), dtype=bool)
    for t in range(1, len(macd)):
        if not np.isfinite(macd[t-1:t+1]).all():
            continue
        if not np.isfinite(signal[t-1:t+1]).all():
            continue
        bullish[t] = (
            macd[t] > signal[t]
            and macd[t-1] <= signal[t-1]
        )

        bearish[t] = (
            macd[t] < signal[t]
            and macd[t-1] >= signal[t-1]
        )

    return bullish, bearish