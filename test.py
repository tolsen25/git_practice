import pandas

class Product:
    def __init__(self, productID, productName, productPrice):
        self.productID = productID
        self.productName = productName
        self.productPrice = productPrice
    
    def discountPrice(percent):
        return self.productPrice - self.productPrice * percent 
    
    def changePrice(price):
        self.productPrice = price

prod = Product("aProduct","name",1)


print(prod.productName)


print()










