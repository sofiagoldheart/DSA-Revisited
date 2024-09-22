class Coffee:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type
        
first_coffee = Coffee ('Macchiato')
second_coffee = Coffee ('Espresso')

print ('First coffee is a:', first_coffee.get_type())
print ('Second coffee is a:', second_coffee.get_type())

first_coffee.set_type ('Cappuccino')

print ('\nFirst coffee is now a', first_coffee.get_type())
print ('Second coffee is still a', second_coffee.get_type())