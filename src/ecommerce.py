    ## Importerar funktionerna load_data och total_revenue från io_utils och metrics.

from io_utils import load_data
from metrics import total_revenue
    
data = load_data('data/ecommerce_sales.csv')

total = total_revenue(data)
print(f'Total revenue: {total}')