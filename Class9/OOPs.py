# Class:

class Car:
    def __init__(self, wheels, sheets, colors, fuel, name):  # Contructor
        self.no_of_wheels = wheels
        self.no_of_sheets = sheets
        self.color = colors
        self.fuel_type = fuel
        self.obj_name = name

        print("I'm Contructor")

    def __str__(self):
        return self.obj_name
        
    def speed_of_car(self):
        print("My car wheels is: ", self)

    def __del__(self):
        print("It's a destructor")
        # pass

honda = Car(5, 7, "red", "Petrol", "Honda")

honda.speed_of_car()

hyundai = Car(4, 5, "black", "Disel", "Hyundai")

hyundai.speed_of_car()