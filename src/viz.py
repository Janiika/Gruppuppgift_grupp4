import pandas as pd
import matplotlib.pyplot as plt
import metrics

def plot_revenue_per_category(summary):
    categories = [row["category"] for row in summary]
    totals = [row["total"] for row in summary]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(categories, totals)
    ax.set_title("Total revenue per category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue")
    ax.grid(True, axis="y")
    plt.tight_layout
    plt.show()

