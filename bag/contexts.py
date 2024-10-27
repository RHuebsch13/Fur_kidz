from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    grand_total = 0  # Initialize grand_total

    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product_price = Decimal(item_data['price'])  
        quantity = item_data['quantity']  
        
        # Calculate totals
        total += product_price * quantity
        grand_total += total  
        product_count += quantity  

        # Append bag items
        bag_items.append({
            'id': item_id,
            'price': product_price,
            'quantity': quantity,
            'subtotal': product_price * quantity,  
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total, 
    }

    return context
