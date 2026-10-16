    ## Importerar funktionerna load_data och total_revenue från io_utils och metrics.

from io_utils import load_data
from metrics import total_revenue

    ## Header leder till att vi kan hämta data från kolumnerna i CSV filen bara med kolumnnamnet genom header-index('kolumnnamn').
    ## Behöver inte veta vilken position kolumnen har, bara kolumnnamnet. Så vi kan skippa att använda t.ex. [1] för att hämta datan.
    
header, data = load_data('data/ecommerce_sales.csv')

total = total_revenue(header, data)
print(f'Total revenue: {total}')