import pandas as pd
import matplotlib.pyplot as plt
import metrics

def plot_revenue_per_column(summary, column, title):
    groups = [row["group"] for row in summary]
    totals = [row["total"] for row in summary]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(groups, totals)
    ax.set_title(title)
    ax.set_xlabel(column)
    ax.set_ylabel("Revenue")
    ax.ticklabel_format(style="plain", axis="y")
    ax.grid(True, axis="y")
    plt.tight_layout()
    plt.show()

