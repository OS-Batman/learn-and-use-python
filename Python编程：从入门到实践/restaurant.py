class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    def open_restaurant(self):
        print(self.name+" is open")
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['strawberry flavor','chocolate flavor','apple flavor']
    def show_flavor(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())