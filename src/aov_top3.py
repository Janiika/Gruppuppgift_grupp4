# Beräknar AOV: total intäkt delat med antal unika order.
from metrics import get_total

def average_order_value(data):
    total = get_total(data, "revenue")
    order_ids = set()
    for row in data:
        order_ids.add(row["order_id"])

    order_count = len(order_ids)
    return total / order_count
