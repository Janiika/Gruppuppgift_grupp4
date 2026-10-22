
    ## Räknar ut totala revenue från CSV-filen.
def total_revenue(data):
    total = 0
    for row in data:
        total += float(row['revenue'])
    return total