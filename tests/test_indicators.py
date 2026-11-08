
import numpy as np
import pytest

from src.ema import calculate_ema
from src.macd import calculate_macd
from src.signals import detect_crossovers


# ==========================================
# TESTS FOR EMA
# ==========================================

def test_ema_calculation():
    prices = np.array([1, 2, 3, 4, 5], dtype=float)

    ema = calculate_ema(prices, period=3)

    # SMA initialisation: (1 + 2 + 3) / 3 = 2
    assert np.isnan(ema[0])
    assert np.isnan(ema[1])
    assert ema[2] == pytest.approx(2.0)

    # alpha = 2 / (3 + 1) = 0.5
    assert ema[3] == pytest.approx(3.0)
    assert ema[4] == pytest.approx(4.0)


def test_ema_invalid_period():
    prices = np.array([10, 20, 30], dtype=float)

    with pytest.raises(ValueError):
        calculate_ema(prices, period=0)


def test_ema_insufficient_data():
    prices = np.array([10, 20], dtype=float)

    with pytest.raises(ValueError):
        calculate_ema(prices, period=3)


# ==========================================
# TESTS FOR MACD
# ==========================================

def test_macd_calculation():
    prices = np.arange(1, 21, dtype=float)

    result = calculate_macd(
        prices,
        fast=2,
        slow=3,
        signal_period=2
    )

    ema_fast = calculate_ema(prices, 2)
    ema_slow = calculate_ema(prices, 3)

    expected_macd = ema_fast - ema_slow

    np.testing.assert_allclose(
        result["macd"],
        expected_macd,
        equal_nan=True
    )


def test_macd_histogram():
    prices = np.arange(1, 21, dtype=float)

    result = calculate_macd(
        prices,
        fast=2,
        slow=3,
        signal_period=2
    )

    expected_histogram = result["macd"] - result["signal"]

    np.testing.assert_allclose(
        result["histogram"],
        expected_histogram,
        equal_nan=True
    )


def test_macd_invalid_parameters():
    prices = np.arange(1, 21, dtype=float)

    with pytest.raises(ValueError):
        calculate_macd(prices, fast=3, slow=2)


# ==========================================
# TESTS FOR CROSSOVER DETECTION
# ==========================================

def test_crossover_detection():
    macd = np.array([np.nan, 0.4, 0.7, 0.3, 0.8])
    signal = np.array([np.nan, 0.5, 0.6, 0.4, 0.6])

    bullish, bearish = detect_crossovers(macd, signal)

    expected_bullish = np.array(
        [False, False, True, False, True]
    )

    expected_bearish = np.array(
        [False, False, False, True, False]
    )

    np.testing.assert_array_equal(bullish, expected_bullish)
    np.testing.assert_array_equal(bearish, expected_bearish)


def test_crossover_different_array_lengths():
    macd = np.array([1, 2, 3])
    signal = np.array([1, 2])

    with pytest.raises(ValueError):
        detect_crossovers(macd, signal)
