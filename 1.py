class CellPhone:
    def __init__(self):
        self.manufact = 'None'
        self.model = 'None'
        self.retail_price = 0


    def set_manufact(self):
        print('Manufacturer:', self.manufact)



    def set_model(self):
        print('Model Number:', self.model)


    def set_retail_price(self):
        print('Retail Price: $%.2f' % self.retail_price)



    def get_manufact(self):
        self.manufact = input('Enter the manufacturer: ')



    def get_model(self):
        self.model = input('Enter model number: ')


    def get_retail_price(self):
        self.retail_price = float(input('Enter the retail price: '))


cellphone = CellPhone()
cellphone.get_manufact()
cellphone.get_model()
cellphone.get_retail_price()

print('Here is the data that you entered:')

cellphone.set_manufact()
cellphone.set_model()
cellphone.set_retail_price()