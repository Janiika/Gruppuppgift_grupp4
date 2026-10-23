    ## Importerar funktionerna från io_utils och metrics.

from io_utils import load_data
from metrics import total_revenue, revenue_per_category
    
data = load_data('data/ecommerce_sales.csv')

total = total_revenue(data)
print(f'Total revenue: {total}')


total_per_category = revenue_per_category(data)
print("Revenue per category:")
for row in total_per_category:
    print(f"{row["category"]}: {row["total"]}")

