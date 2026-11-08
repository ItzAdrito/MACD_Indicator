import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_macd_dashboard(
    dates,
    prices,
    ema_fast,
    ema_slow,
    macd,
    signal,
    histogram,
    bullish,
    bearish,
    title="MACD Analysis"
):

    # Colour palette
    bg = "#101B2B"
    panel = "#172538"
    cyan = "#48B8E8"
    orange = "#F4A64A"
    green = "#35D39A"
    red = "#F16D75"
    text = "#DCE6F1"
    muted = "#91A3B8"

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10
    })

    fig, axes = plt.subplots(
        3, 1,
        figsize=(16, 10),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 2, 1.5]}
    )

    fig.patch.set_facecolor(bg)

    ax1, ax2, ax3 = axes

    for ax in axes:
        ax.set_facecolor(panel)
        ax.tick_params(colors=muted)
        ax.grid(
            True,
            color="#344256",
            linestyle="--",
            linewidth=0.6,
            alpha=0.65
        )

        for spine in ax.spines.values():
            spine.set_color("#344256")

        ax.yaxis.label.set_color(text)

    # -------------------------
    # 1. PRICE CHART
    # -------------------------

    ax1.plot(
        dates, prices,
        color=cyan,
        linewidth=1.7,
        label="Close Price"
    )

    ax1.plot(
        dates, ema_fast,
        color=green,
        linewidth=1.2,
        label="EMA 12"
    )

    ax1.plot(
        dates, ema_slow,
        color=orange,
        linewidth=1.2,
        label="EMA 26"
    )

    ax1.scatter(
        dates[bullish],
        prices[bullish],
        marker="^",
        color=green,
        s=65,
        label="Bullish Crossover",
        zorder=5
    )

    ax1.scatter(
        dates[bearish],
        prices[bearish],
        marker="v",
        color=red,
        s=65,
        label="Bearish Crossover",
        zorder=5
    )

    ax1.set_title(
        "PRICE ACTION & MOVING AVERAGES",
        color=text,
        loc="left",
        fontsize=11,
        fontweight="bold",
        pad=12
    )

    ax1.legend(
        facecolor=panel,
        edgecolor="#344256",
        labelcolor=text,
        loc="upper left",
        ncol=3
    )

    # -------------------------
    # 2. MACD CHART
    # -------------------------

    ax2.plot(
        dates, macd,
        color=cyan,
        linewidth=1.6,
        label="MACD"
    )

    ax2.plot(
        dates, signal,
        color=orange,
        linewidth=1.5,
        label="Signal"
    )

    ax2.axhline(
        0,
        color=muted,
        linestyle="--",
        linewidth=0.8
    )

    ax2.scatter(
        dates[bullish],
        macd[bullish],
        marker="^",
        color=green,
        s=45,
        zorder=5
    )

    ax2.scatter(
        dates[bearish],
        macd[bearish],
        marker="v",
        color=red,
        s=45,
        zorder=5
    )

    ax2.set_title(
        "MACD & SIGNAL LINE",
        color=text,
        loc="left",
        fontsize=11,
        fontweight="bold",
        pad=12
    )

    ax2.legend(
        facecolor=panel,
        edgecolor="#344256",
        labelcolor=text,
        loc="upper left"
    )

    # -------------------------
    # 3. HISTOGRAM
    # -------------------------

    bar_colors = np.where(
        histogram >= 0,
        green,
        red
    )

    ax3.bar(
        dates,
        histogram,
        color=bar_colors,
        width=0.8,
        alpha=0.85
    )

    ax3.axhline(
        0,
        color=muted,
        linewidth=0.8
    )

    ax3.set_title(
        "MACD HISTOGRAM",
        color=text,
        loc="left",
        fontsize=11,
        fontweight="bold",
        pad=12
    )

    # -------------------------
    # FINAL FORMATTING
    # -------------------------

    ax3.xaxis.set_major_locator(
        mdates.AutoDateLocator()
    )

    ax3.xaxis.set_major_formatter(
        mdates.ConciseDateFormatter(
            ax3.xaxis.get_major_locator()
        )
    )

    ax3.set_xlabel("Date", color=text)

    fig.suptitle(
        title,
        color=text,
        fontsize=17,
        fontweight="bold",
        x=0.08,
        ha="left"
    )

    fig.tight_layout(
        rect=[0, 0, 1, 0.96]
    )

    plt.savefig(
        "../plots/nifty50_macd.png",
        dpi=300,
        bbox_inches="tight",
        facecolor=bg
    )

    plt.show()