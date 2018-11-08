






pending_orders = []
delivered_order = [1,2,12.10]

def check_order_status(order_id):
    if order_id in delivered_order:
        return True
    else:
        return False