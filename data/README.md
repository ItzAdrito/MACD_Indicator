# Data

This directory contains the historical market data used for the technical indicator analysis.

## Dataset: NIFTY 50

| Attribute | Details |
|---|---|
| Index | NIFTY 50 |
| Data Source | Yahoo Finance |
| Ticker Symbol | `^NSEI` |
| Frequency | Daily |
| Data Type | Historical OHLCV data |
| Time Period | Approximately 5 years |
| Format | CSV |

## Data Description

The dataset contains historical NIFTY 50 market information, including:

- **Open:** Opening index value.
- **High:** Highest index value during the trading session.
- **Low:** Lowest index value during the trading session.
- **Close:** Closing index value.
- **Volume:** Reported trading volume, where available.

The closing price is used as the primary input for calculating technical indicators such as EMA and MACD.

## Data Acquisition

The data was retrieved using the Yahoo Finance Python library (`yfinance`).

Ticker: `^NSEI`

The dataset is downloaded programmatically and stored locally for analysis.

## Notes

- The dataset is historical market data and may be updated periodically.
- Missing values and data formatting are handled during preprocessing.
- This dataset is used strictly for educational and quantitative research purposes.
- Historical market behaviour does not guarantee future performance.

## Reproducibility

To retrieve the dataset again, install `yfinance`:

```bash
pip install yfinance
```

**Source:** [Yahoo Finance – NIFTY 50](https://finance.yahoo.com/quote/%5ENSEI/)