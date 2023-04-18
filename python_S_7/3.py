class Car :
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def info(self):
        print("Model : ", self.model, ", Color : ", self.color)
bmw = Car("BMW", "white")
bmw.info()