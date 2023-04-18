class Car : 
    count = 0
    speed = 0
    def speedChange(self, v):
        Car.count += 1
        self.speed = v
bmw = Car()
benz = Car()
bmw.speedChange(100)
print("bmw speed :", bmw.speed)
print("number of speedChange :", Car.count)
benz.speedChange(120)
print("Benz speed :", benz.speed)
print("number of speedChange :", Car.count)