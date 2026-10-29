
    ## Funktion som räknar ut totalt antal från en kolumn
def get_total(data, column):
    total = 0

    for row in data:
        total += float(row[column])

    return total


    ## Räknar ut totala intäkten per valfri kolumn
def revenue_per_column(data, column):
    totals = {}
    
    for row in data:
        group = row[column]
        total = float(row["revenue"])

        if group not in totals:
            totals[group] = total
        else:
            totals[group] += total

    summary = []

    for group, total in totals.items():
        summary.append({
            "group": group,
            "total": total
        })

    return summary
