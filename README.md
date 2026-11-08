# Technical Indicators from Scratch: EMA and MACD

## Project Overview

This project explores the mathematical foundations and Python implementation of two fundamental tools used in technical analysis: the Exponential Moving Average (EMA) and the Moving Average Convergence Divergence (MACD) indicator.

The primary objective is to understand how these indicators are constructed mathematically, implement them from scratch using NumPy, and visualise their behaviour using Python.

The project begins with synthetic price data to understand the behaviour of the indicators under different market conditions. It then applies the same implementation to historical NIFTY 50 data to examine how the indicators behave on a real financial time series.

## Objectives

- Understand the mathematical foundations of exponential moving averages.
- Implement EMA without relying on pre-built technical analysis libraries.
- Construct the MACD line, signal line and histogram.
- Identify bullish and bearish MACD crossovers.
- Visualise the indicators alongside historical price movements.
- Compare indicator behaviour under synthetic and historical market conditions.

## Mathematical Foundations

### 1. Exponential Moving Average (EMA)

An Exponential Moving Average assigns greater weight to recent observations while gradually reducing the weight assigned to older observations.

The recursive formula is:

EMA(t) = α × P(t) + (1 - α) × EMA(t-1)

where:

α = 2 / (N + 1)

P(t) represents the current price, and N represents the EMA period.

For initialisation, this project uses the Simple Moving Average of the first N observations.

### 2. Moving Average Convergence Divergence (MACD)

MACD is a momentum indicator constructed using two exponential moving averages.

The standard MACD configuration uses:

- Fast EMA: 12 periods
- Slow EMA: 26 periods
- Signal EMA: 9 periods

MACD Line = EMA(12) - EMA(26)

Signal Line = EMA(9) of the MACD Line

MACD Histogram = MACD Line - Signal Line

### 3. Crossover Detection

The project identifies two types of MACD crossovers:

Bullish Crossover:
The MACD line moves above the signal line.

Bearish Crossover:
The MACD line moves below the signal line.

These crossovers are commonly interpreted as momentum signals. However, they are lagging indicators and do not guarantee future price movements.

## Implementation

The project is implemented in Python using:

- NumPy for numerical computations.
- Matplotlib for data visualisation.
- Pandas for historical financial data handling.
- yfinance for retrieving historical market data.

The implementation is divided into modular functions:

1. calculate_ema(): Computes the Exponential Moving Average.
2. calculate_macd(): Computes the MACD line, signal line and histogram.
3. detect_crossovers(): Identifies bullish and bearish crossover points.

The implementation uses an SMA-based initialisation for EMA calculations. Consequently, the initial observations are represented using NaN values until sufficient data is available.

## Experiments

### Experiment 1: Synthetic Price Data

Synthetic price observations are used to examine the behaviour of EMA and MACD under different market conditions, including:

- Sideways price movement.
- Sustained bullish movement.
- Bearish reversal.
- Bullish recovery.
- Consolidation.

This experiment helps illustrate how the MACD line, signal line and histogram respond to changes in price momentum.

### Experiment 2: Historical NIFTY 50 Data

The same indicator implementation is applied to historical daily NIFTY 50 index data.

This experiment examines:

- The relationship between price movements and moving averages.
- MACD behaviour during bullish and bearish market phases.
- The occurrence and timing of bullish and bearish crossovers.
- The lag between price movements and indicator signals.

The purpose is to study indicator behaviour on historical data, not to establish a profitable trading strategy.

## Visualisation

The project includes visualisations of:

1. Closing price.
2. MACD line and signal line.
3. MACD histogram.
4. Bullish and bearish crossover markers.

The plots help examine the relationship between price momentum and the behaviour of the MACD indicator.

## Limitations

- MACD is a lagging indicator and may generate signals after a price movement has already begun.
- Crossover signals can be unreliable during sideways market conditions.
- Historical indicator behaviour does not guarantee future performance.
- The project does not account for transaction costs, slippage or execution constraints.
- No claim of trading profitability is made.

## Future Improvements

- Implement additional technical indicators such as RSI and Bollinger Bands.
- Develop a backtesting engine.
- Calculate cumulative returns, volatility, Sharpe ratio and maximum drawdown.
- Incorporate transaction costs and slippage.
- Explore momentum and mean-reversion strategies.
- Conduct more rigorous statistical analysis of indicator performance.

## Technologies Used

Python | NumPy | Pandas | Matplotlib | yfinance

## Disclaimer

This is an educational quantitative finance project intended to explore financial mathematics, numerical computation and historical market data analysis. It is NOT financial advice or a recommendation to buy or sell any financial instrument. It is NOT intended for commercial use. It is NOT intended for live trading or investment decisions.