class CellPhone:
    def __init__(self):
        self.manufact = 'none'
        self.model = 'none'
        self.retail_price = 0

    def set_manufact(self, manufact):
        new_manufact = input('Enter the new manufacturer: ')
        manufact.replace(self.manufact, new_manufact)
        
    def set_model(self, model):
        new_model = input('Enter the new model: ')
        model.replace(self.model, new_model)

    def set_retail_price(self, retail_price):
        new_retail_price = input('Enter a new retail price: ')
        retail_price.replace(self.retail_price, new_retail_price)

    def get_manufact(self):
        print('Manufacturer: %s' % self.manufact)

    def get_model(self):
        print('Model Number: %s' % self.model)

    def  get_retail_price(self):
        print('Retail Price $%.2f' % self.retail_price)

cell_phone = CellPhone()

cell_phone.manufact = input('Enter the manufacturer: ')
cell_phone.model = input("Enter the model number: ")
cell_phone.retail_price = float(input("Enter the retail price: "))
cell_phone.set_model(cell_phone.model)
print("Here is the data that you entered:")
cell_phone.get_manufact()
cell_phone.get_model()
cell_phone.get_retail_price()