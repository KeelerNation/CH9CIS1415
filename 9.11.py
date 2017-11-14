class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ $%d = $%d' % (self.item_price, self.item_price * self.item_quantity))

    def print_item_description(self):

        print('%s: %s'% (self.item_name, self.item_description))



class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2016"
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item):
        if item != self.cart_items:
            print('Item not found in cart')
        else:
            self.cart_items.remove(item)
    #def modify_item(self):

    def get_num_items_in_cart(self):
         return self.cart_items

    #def get_cost_of_cart(self):

    #def print_total(self):

    #def print_description(self):

    def print_cart(self):
        pass


if __name__ == "__main__":

    items1 = ItemToPurchase()
    print('Item 1')
    items1.item_name = input('Enter the item name:\n')
    items1.item_price = float(input('Enter the item price:\n'))
    items1.item_quantity = int(input('Enter the item quantity:\n'))
    items1.item_description = input('Enter item description\n')
    items1.print_item_description()

    cart1 = ShoppingCart()

    cart1.add_item(items1)
    print(cart1.cart_items)


    print('')
    items2 = ItemToPurchase()
    print('Item 2')
    items2.item_name = input('Enter the item name:\n')
    items2.item_price = float(input('Enter the item price:\n'))
    items2.item_quantity = int(input('Enter the item quantity:\n'))
    items2.item_description = input('Enter item description:\n')
    items2.print_item_description()

    print('')
    print('TOTAL COST')
    #items1.print_item_cost()
    items2.print_item_cost()

    print('')

    print('Total: $%d' % ((items1.item_quantity * items1.item_price) + (items2.item_price * items2.item_quantity)))

