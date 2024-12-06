class Boat:
    def __init__(self,model, year):
        self.model = model
        self.year = year
        self.__speed = 0 # jak dodaliśmy __ to zostało zahermatyzowane i jest prywatne

    def sail(self):
        self.__speed += 10

    def speedometr(self):
        print(f'Prędkość wynosi {self.__speed} knots')

boat = Boat("Sportina", 2024)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# print(boat.__speed) # 50
# Po dodaniu __ - pole prywatne AttributeError: 'Boat' object has no attribute '__speed'
boat.speedometr() # Prędkość wynosi 50 knots
boat.__speed = 10
boat.speedometr()
# Prędkość wynosi 50 knots