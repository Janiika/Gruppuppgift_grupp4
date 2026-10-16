
    ## Räknar ut totala revenue från CSV-filen.
def total_revenue(header, data):
    revenue_index = header.index('revenue')
    total = 0
    for row in data:
        total += float(row[revenue_index])
    return total