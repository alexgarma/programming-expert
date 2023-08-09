class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count = 0

    def add_item(self, name, price, quantity):
        if ( self.item_count + quantity <= self.max_capacity ) and (name not in self.items) :
            item = {
                "price" : price,
                "quantity": quantity
            }
            self.items[name] = item
            self.item_count += quantity
            return True
        else:
            return False

    def delete_item(self, name):
        if name in self.items:
            self.item_count += - self.items[name]["quantity"]
            del self.items[name]
            return True
        else:
            return False

    def get_items_in_price_range(self, min_price, max_price):
        items_in_price_range = []
        for key,value in self.items.items():
            if value.get("price") >= min_price and value.get("price") <= max_price:
                items_in_price_range.append(key)
        return items_in_price_range


    def get_most_stocked_item(self):
        if len(self.items) > 0:
            return sorted(self.items,reverse = True, key = lambda key: self.items.get(key).get("quantity"))[0]
        else:
            return None