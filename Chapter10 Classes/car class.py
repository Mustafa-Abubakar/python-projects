class Car:
    def __init__(self, model, color, company, speed):
        self.speed = speed
        self.model = model
        self.color = color
        self.company = company
    
    def info(self):
        return self.model, self.color, self.company, self.speed
    
toyota = Car('Toyota', 'white', 'Toyota', '65km/hr')
print(toyota.info())