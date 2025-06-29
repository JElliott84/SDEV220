#Created by: Jason Elliott
#Lists, Functions, and Classes 
#This app will use a superclass(Vehicle), a subclass(Automobile) and allow input where the app will then ask for other attributes to put into a format. 
class Vehicle:
    def __init__(self,vtype):
        self.vtype = vtype
class Automobile(Vehicle):
    def __init__(self, vtype, year, make, model, doorcount, roof):
        super().__init__(vtype)
        self.year = year
        self.make = make
        self.model = model
        self.doorcount = doorcount
        self.roof = roof

def your_veh():
    vtype = "Car"
    year = input("What is the year of your car?:")
    make = input("What is the make of your car?:")
    model = input("What is the model of your car?:")
    doorcount = input("How many doors does your car have, 2,3,4,5?:")
    roof = input ("What is your roof made of?:")
    car = Automobile(vtype, year, make, model, doorcount, roof)
    return car

def info(car_object):
    print("Your Vehicle Type:", car.vtype)
    print("Your year:", car.year)
    print("Your make and model:", car.make, car.model)
    print("Your car has",car.doorcount, "doors" )
    print("Your roof is", car.roof)

#This begins the actual program in order to execute. Had issues with some of the indents and parameters, but figured it out once I seen the syntax error. 
car = your_veh()

print("Your Car information:")

info(car)