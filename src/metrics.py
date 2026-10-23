
    ## Räknar ut totala revenue från CSV-filen.
def total_revenue(data):
    total = 0
    for row in data:
        total += float(row['revenue'])
    return total


    ## Räknar ut totala intäkten per kategori.
def revenue_per_category(data):
    totals = {}
    
    for row in data:
        category = row["category"]
        total = float(row["revenue"])

        if category not in totals:
            totals[category] = total
        else:
            totals[category] += total

    summary = []

    for category, total in totals.items():
        summary.append({
            "category": category,
            "total": total
        })

    return summary
